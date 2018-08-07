from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.addbooks),
    url(r'^remove/(?P<x>\d+)$', views.remove),
    # url(r'^removeconfirm/(?P<id>\d+)$', views.removeconfirm),
    # url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard),
    # url(r'^shoes$', views.shoes),
    # url(r'^logout$', views.logout),
    # url(r'^buy/(?P<id>\d+)$', views.buy),
    # url(r'^sell$', views.sell),
]
