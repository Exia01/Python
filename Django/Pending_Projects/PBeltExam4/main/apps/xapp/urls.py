from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexlogin), #start as login
    url(r'^register$', views.register),#register page
    url(r'^create$', views.createuser), #registers the user
    url(r'^dashboard/$', views.dashboard),#main page
    url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard), #dashboard redirect with user.
    url(r'^delete/(?P<x>\d+)$', views.delete),# Deletes a appointment 
    url(r'^edit/(?P<x>\d+)$', views.edit),# Deletes a appointment 
    
    url(r'^loginprocess$', views.loginprocess), #logs in the user
    url(r'^update$', views.update), #logs in the user
    url(r'^add/(?P<x>\d+)$', views.add),# add the trip process
    url(r'^add$', views.add),# add the trip process
    url(r'^logout$', views.logout),#log out
]
#  url(r'^showappointment/(?P<x>\d+)$', views.showappointment),# show a appointment 