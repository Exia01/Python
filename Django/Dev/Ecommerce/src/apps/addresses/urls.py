from django.conf.urls import url
from .views import (
    checkout_address_create_view,
    checkout_address_reuse_view,
    )


urlpatterns = [
    url(r'^create$',checkout_address_create_view, name='checkout_address_create'),
    url(r'^reuse$',checkout_address_reuse_view, name='checkout_address_reuse'),
]
