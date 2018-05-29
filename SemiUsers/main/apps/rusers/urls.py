from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^adduser$', views.add),
    url(r'^(?P<x>\d+)/edit$', views.edit),
    url(r'^(?P<x>\d+)/show', views.show),
    url(r'^(?P<x>\d+)/update$', views.update),
    url(r'^process$', views.process),
    url(r'^(?P<x>\d+)/delete$', views.delete),
]
