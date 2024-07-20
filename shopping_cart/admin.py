from django.contrib import admin
from .models import Product, CartItem, orders

# Register your models here.


 
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(orders)
