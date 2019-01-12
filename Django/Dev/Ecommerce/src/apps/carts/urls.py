from django.conf.urls import url

from .views import (
        cart_home, 
        cart_update, 
        checkout_home,
        checkout_done_view,

        # api routes
        cart_detail_api_view,
        )

urlpatterns = [
    # regular routes
    url(r'^$', cart_home, name='home'),
    url(r'^update/$', cart_update, name='update'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),

     #API routes 
    url(r'^update/cart$', cart_detail_api_view, name='cart-update'),
]