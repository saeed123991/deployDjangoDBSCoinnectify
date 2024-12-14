from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def currency_converter(request):
    if request.method == 'POST':
        crypto = request.POST.get('crypto', '').lower()
        currency = request.POST.get('currency', '').lower()

        # Validate Input
        if not crypto or not currency:
            return render(request, 'crypto/currency_rate.html', {'error': 'Both cryptocurrency and currency are required!'})

        # Fetch Rates from CoinGecko API
        api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"
        response = requests.get(api_url)

        if response.status_code == 200:
            rates = response.json()
            if crypto in rates and currency in rates[crypto]:
                rate = rates[crypto][currency]
                return render(request, 'crypto/currency_rate.html', {
                    'crypto': crypto.capitalize(),
                    'currency': currency.upper(),
                    'rate': rate
                })
            else:
                return render(request, 'crypto/currency_rate.html', {'error': f"Invalid cryptocurrency or currency: {crypto}/{currency}"})
        else:
            return render(request, 'crypto/currency_rate.html', {'error': "Failed to fetch conversion rates. Please try again later."})
    
    return render(request, 'crypto/currency_rate.html')
