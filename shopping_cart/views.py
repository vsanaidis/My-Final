from django.shortcuts import render, redirect
from .models import Product, CartItem, orders
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.shortcuts import render, get_object_or_404
# Create your views here.


# here I create my view of the product_list which retrieves all the products from my tables and renders the subscriptions.html
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'subscriptions.html', {'products': products})
#I create my viewcart that displays what is in the user's shopping cart
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
 # I create a view to add products to each user's cart 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')
 # just another view that removes the items
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')
#a view that will make the buying
def buy(request, product_id=None):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            
            if product_id:
                product = get_object_or_404(Product, id=product_id)
                # Assuming you want to handle a single product
                order.product = product
                order.quantity = 1  # Or however you want to handle quantity
            else:
                # Handle case when buying all items in the cart
                cart_items = CartItem.objects.filter(user=request.user)
                for item in cart_items:
                    order.product = item.product
                    order.quantity = item.quantity
                    order.save()
                # Optionally clear cart
                CartItem.objects.filter(user=request.user).delete()

            return redirect('cart:order_confirmed', order_id=order.id)
    else:
        form = OrderForm()

    if product_id:
        products = [get_object_or_404(Product, id=product_id)]
    else:
        products = []

    return render(request, 'buy.html', {'form': form, 'products': products})
#a form that gets the order_id and returns the render of order_confirmed.html
def order_confirmed(request, order_id):
    order = get_object_or_404(orders, id=order_id)
    return render(request, 'order_confirmed.html', {'order': order})