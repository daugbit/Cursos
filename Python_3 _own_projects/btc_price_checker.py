import requests
import time
from os import system
from datetime import date, datetime

def get_bitcoin_price_usd():
  url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
  response = requests.get(url)
  data = response.json()
  return data['bitcoin']['usd']

def get_bitcoin_price_brl():
  url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl'
  response = requests.get(url)
  data = response.json()
  return data['bitcoin']['brl']

def calculate_sats_per_dollar(price):
  sats_per_dollar = 100000000 / price
  return sats_per_dollar

def calculate_sats_per_real(price):
  sats_per_real = 100000000 / price
  return sats_per_real

while True:
  system("clear")
  price_usd = get_bitcoin_price_usd()
  sats_usd = calculate_sats_per_dollar(price_usd)
  price_brl = get_bitcoin_price_brl()
  sats_brl = calculate_sats_per_dollar(price_brl)
  print(date.today(), datetime.now().strftime("%H:%M:%S"))
  print(f"${price_usd:,.0f}", "-", f"{sats_usd:.0f} sats per dollar")
  print(f"R${price_brl:,.0f}", "-", f"{sats_brl:.0f} sats per real")
  time.sleep(60)  # Aguarda 60 segundos (1 minuto)