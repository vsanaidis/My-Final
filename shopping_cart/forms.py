from .models import orders
from django import forms
from .models import Product
#my model for my shopping cart
class OrderForm(forms.ModelForm):
    class Meta:
        model = orders #the model I use is orders
        fields = ['address', 'payment_method']#the fields for the user that are his/her address location and payment method dropdown.