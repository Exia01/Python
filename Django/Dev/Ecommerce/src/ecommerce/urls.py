"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^about/$', views.about_page, name='about'),
    url(r'^contact/$', views.contact_page, name='contact'),
    url(r'^products/', include(('apps.products.urls', 'products'), namespace='products')),
    url(r'^search/', include(('apps.search.urls', 'search'), namespace='search')),
    url(r'^cart/', include(('apps.carts.urls', 'cart'), namespace='cart')),
    url(r'^checkout/address/create/', include(('apps.addresses.urls', 'address'), namespace='address')),
    url(r'^accounts/', include(('apps.accounts.urls', 'account'), namespace='account')),
    url('admin/', admin.site.urls),
    # Test pages
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:  # If it is in debug mode
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 # url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
