from django.conf.urls import url
from .views import (
    login_page,
    register_page,
    )


urlpatterns = [
    url(r'^register/$',register_page, name='register'),
    url(r'^login/$',login_page, name='login'),
]
