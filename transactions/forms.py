import datetime

from django import forms
from django.conf import settings

from .models import Transaction


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)

        self.fields['transaction_type'].disabled = True
        self.fields['transaction_type'].widget = forms.HiddenInput()

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    secret_key = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your secret key'}),
        required=True,
        label="Secret Key"
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # Pass the user object to the form
        super().__init__(*args, **kwargs)

    def clean_secret_key(self):
        secret_key = self.cleaned_data.get('secret_key')
        if not self.user.check_password(secret_key):  # Validate the secret key
            raise forms.ValidationError("Invalid secret key. Please try again.")
        return secret_key


class WithdrawForm(TransactionForm):
    wallet_address = forms.CharField(
        required=True,
        label="Wallet Address",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Wallet Address'})
    )
    method = forms.ChoiceField(
        choices=[('TRC20', 'TRC20'), ('BNB Smart Chain', 'BNB Smart Chain')],
        required=True,
        label="Payment Method"
    )

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = settings.MINIMUM_WITHDRAWAL_AMOUNT
        max_withdraw_amount = account.account_type.maximum_withdrawal_amount
        balance = account.balance

        amount = self.cleaned_data.get('amount')

        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance:
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You cannot withdraw more than your account balance'
            )

        return amount




class TransactionDateRangeForm(forms.Form):
    daterange = forms.CharField(required=False)

    def clean_daterange(self):
        daterange = self.cleaned_data.get("daterange")
        print(daterange)

        try:
            daterange = daterange.split(' - ')
            print(daterange)
            if len(daterange) == 2:
                for date in daterange:
                    datetime.datetime.strptime(date, '%Y-%m-%d')
                return daterange
            else:
                raise forms.ValidationError("Please select a date range.")
        except (ValueError, AttributeError):
            raise forms.ValidationError("Invalid date range")
