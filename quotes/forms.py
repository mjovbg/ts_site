from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['ticker']     # fields that you want to put in DB; ticker is from add_stock.html
