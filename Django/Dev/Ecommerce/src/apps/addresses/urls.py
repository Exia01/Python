from django.conf.urls import url
from .views import (
    checkout_address_create_view,
    )


urlpatterns = [
    url(r'^$',checkout_address_create_view, name='checkout_address_create'),
]
