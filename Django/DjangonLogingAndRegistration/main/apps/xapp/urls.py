from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexlogin), #Defined as login
    url(r'^register$', views.register),
    url(r'^dashboard/$', views.landing),
    url(r'^create$', views.create), #registers the user
    url(r'^loginprocess$', views.loginprocess), #logs in the user
#     url(r'^dashboard$', views.dashboard),
#     url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard),
#     url(r'^shoes$', views.shoes),
#     # url(r'^logout$', views.logout),
#     url(r'^buy/(?P<id>\d+)$', views.buy),
#     url(r'^sell$', views.sell),
#     # url(r'^remove$', views.remove),
]
