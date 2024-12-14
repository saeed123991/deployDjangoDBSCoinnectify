from django.urls import path
from . import views

app_name = 'crypto'

urlpatterns = [
    path('currency-converter/', views.currency_converter, name='currency_converter'),
]
