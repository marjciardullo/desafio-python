from symbol import parameters
import symbol
from tkinter import N
import apikey
import requests
import time

headers = {
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts' : 'application/json'
}

params = {
    'start' : '1',
    'convert' : 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

cont = 0

while True:

    json = requests.get(url, params=params, headers=headers).json()

    moedas = json['data']

    for x in moedas:
        if x['symbol'] == 'BTC' or x['symbol'] == 'ETH' or x['symbol'] == 'LTC':
            print(x['symbol']+'USD', x['quote']['USD']['price'])

    cont += 1

    time.sleep(100)

    if cont == 50:

        break



