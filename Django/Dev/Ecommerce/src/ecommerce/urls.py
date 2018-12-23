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

# prodcuts app
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^about/$', views.about_page),
    url(r'^contact/$', views.contact_page),
    url(r'^login/$', views.login_page),
    url(r'^register/$', views.register_page),
    url(r'^products/', include(('apps.products.urls'))),
    url(r'^accounts/$', views.dashboard_page),
    url('admin/', admin.site.urls),
]


if settings.DEBUG:  # If it is in debug mode
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
