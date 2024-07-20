from .models import orders
from django import forms
from .models import Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['address', 'payment_method']