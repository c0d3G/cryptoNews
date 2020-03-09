from django.shortcuts import render

import os

cryptocompare_api = os.environ.get('CRYPTOCOMPARE_API_KEY')

# Create your views here.

def home(request):
    import requests
    import json

    # Get Crypto price

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD&api_key=cryptocompare_api")
    price = json.loads(price_request.content)

    # Get crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN&api_key=cryptocompare_api")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api':api, 'price':price})

# Price search
def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD&api_key=cryptocompare_api")
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})
    else:
        notfound = "Enter crypto currency symbol in to the lookup form above.."
        return render(request, 'prices.html', {'notfound':notfound})