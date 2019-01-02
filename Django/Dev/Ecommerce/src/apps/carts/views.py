from django.shortcuts import render, redirect
from .models import Cart
from ..products.models import Product
from ..orders.models import Order


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    # print(product_id)
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            cart_obj, new_obj = Cart.objects.new_or_get(request)
        except Product.DoesNotExist:
            print("Show message to user, product is gone.")
            return redirect('cart:home')
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    request.session['cart_items'] = cart_obj.products.count()
    return redirect('cart:home')


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    return render(request, 'carts/checkout.html', {'object': order_obj})

"""
request.session.session_key
request.session.set_expiry(300) # 5 minutes
print(request.session.session_key)
 # cart_obj.products.remove(1)
 # cart_obj.products.remove(obj) # this removes an item from a many to many field 
 # product_obj.get_absolute_url() --> property of the product model 

"""
