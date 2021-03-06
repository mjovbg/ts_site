from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

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
    # if the add stock form is filled it will return success message and add stock to DB
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Stock added!'))
            return redirect ('add_stock')
    else:
        # if the form is not filled, it will just print stocks that are already in the db
        ticker = Stock.objects.all()
        output = []     # a list for storing data from DB
        for ticker_item in ticker:
            api_request = requests.get(
                'https://sandbox.iexapis.com/stable/stock/' + str(ticker_item) + '/quote?token=Tpk_6d838c95bd884fbc81acf66dc4cb613b')

            try:
                api = json.loads(api_request.content)
                output.append(api)      # for loop now stores data into the output list!
            except Exception as e:
                api = "Error...."

        return render(request, 'add_stock.html', {'ticker': ticker, 'output':output})   #added dict pair for passing items from the output list

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)       # grabbing id from DB
    item.delete()
    messages.success('Stock Deleted!')
    return redirect(delete_stock)

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker':ticker})

# api_request = requests.get(
#     'https://sandbox.iexapis.com/stable/stock/' + ticker + '/quote?token=Tpk_6d838c95bd884fbc81acf66dc4cb613b')


