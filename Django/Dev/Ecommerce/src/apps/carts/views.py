from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Cart

from ..billing.models import BillingProfile
from ..products.models import Product
from ..orders.models import Order

from ..accounts.models import GuestEmail
from ..accounts.forms import LoginForm, GuestForm

from ..addresses.models import Address
from ..addresses.forms import AddressForm


def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request) # implement value_list()
    products = [{
        "name": x.title,
        "price": x.price,
        "url": x.get_absolute_url(),
        "id":x.id
        } for x in cart_obj.products.all()]  # pulls a results list and perform list comprehension
    cart_data = {"products":products, "subtotal":cart_obj.subtotal, "total":cart_obj.total}
    return JsonResponse(cart_data)


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {"cart": cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')

    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            cart_obj, new_obj = Cart.objects.new_or_get(request)
        except Product.DoesNotExist:
            print("Show message to user, product is gone.")
            return redirect('cart:home')
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added = False
        else:
            cart_obj.products.add(product_obj)
            added = True
    request.session['cart_items'] = cart_obj.products.count()
    if request.is_ajax():
        json_data = {
            "added": added,
            "remove": not added,  # always opposite so true or false
            "cartItemCount": cart_obj.products.count()
        }
        return JsonResponse(json_data)
        # return JsonResponse({"message":"Error 400"}, status=400)
    return redirect('cart:home')


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect('cart:home')

    login_form = LoginForm()
    guest_form = GuestForm()
    address_form = AddressForm()
    
    billing_address_id = request.session.get('billing_address_id', None)
    shipping_address_id = request.session.get('shipping_address_id', None)

    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
 
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated:  
            address_qs = Address.objects.filter(billing_profile=billing_profile)
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = Address.objects.get(id=shipping_address_id)
            # print(order_obj)
            del request.session['shipping_address_id']
        if billing_address_id:
            order_obj.billing_address = Address.objects.get(id=billing_address_id)
            del request.session['billing_address_id']
        if billing_address_id or shipping_address_id:
            order_obj.save()

    if request.method == "POST":
        # check that order is done.
        is_done = order_obj.check_done()
        print(is_done)
        if is_done:
            print('clearing order')
            order_obj.mark_paid()
            del request.session['cart_id']
            del request.session['cart_items']

            return redirect("cart:success")
    context = {
        'object': order_obj,
        'billing_profile': billing_profile,
        'login_form': login_form,
        'guest_form': guest_form,
        'address_form': address_form,
        'address_qs': address_qs,
    }
    return render(request, 'carts/checkout.html', context)



def checkout_done_view(request):
    return render(request, "carts/checkout_done.html", {})
"""
request.session.session_key
request.session.set_expiry(300) # 5 minutes
print(request.session.session_key)
 # cart_obj.products.remove(1)
 # cart_obj.products.remove(obj) # this removes an item from a many to many field 
 # product_obj.get_absolute_url() --> property of the product model 

"""
