"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include  # include imports the module
from django.contrib import admin
from django.urls import path
urlpatterns = [
    # this adds it to a routing path --> blogs_urls
    url(r'^blogs', include('apps.blogs_app.urls')),
    url(r'^blogs/', include('apps.blogs_app.urls')),
    url(r'^$', include('apps.first_app.urls')),
    #the/ adds the fuctionality to divy up the sections.
    url(r'^first_app/', include('apps.first_app.urls')),
    url('admin/', admin.site.urls),
]
