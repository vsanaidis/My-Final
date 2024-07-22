from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#here I specify the payment choices the user has for the dropdown
PAYMENT_CHOICES = (
    ('card', 'Credit Card'),
    ('paypal', 'PayPal'),
)
# the model for my products (subscriptions atm)
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
 
    def __str__(self):
        return self.name
#My model for the items added in the cart
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
# my model for the orders the user has created 
class orders(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)#I justify the choices which are the choices justified at the start of this document
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'