from django.shortcuts import render


# Create your views here.
# for every web page you create one view by creating a function

def home(request):
    # api handling
    import requests     # grabs stuff fro web
    import json

    if request.method == 'POST':
        ticker = str(request.POST['ticker'])       # ticker is the name you gave to the form in base.html
        api_request = requests.get(
            'https://sandbox.iexapis.com/stable/stock/'+ ticker + '/quote?token=Tpk_6d838c95bd884fbc81acf66dc4cb613b')
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error...."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    return render(request, 'add_stock.html', {})

# ticker = request.POST['ticker']
# api_request = requests.get(
#     'https://sandbox.iexapis.com/stable/stock/' + ticker + '/quote?token=Tpk_6d838c95bd884fbc81acf66dc4cb613b')

