from django.shortcuts import render
from .models import Cart

def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html")

"""
request.session.session_key
request.session.set_expiry(300) # 5 minutes
print(request.session.session_key)

"""
