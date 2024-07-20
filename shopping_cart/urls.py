from django.urls import path
from . import views
 
app_name = 'cart'
 
urlpatterns = [
    path('subscriptions/', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('buy/', views.buy, name='buy'),  # For buying all items in the cart
    path('buy/<int:product_id>/', views.buy, name='buy'),
    path('order_confirmed/<int:order_id>/', views.order_confirmed, name='order_confirmed'),
]
