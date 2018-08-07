from django.conf.urls import url
from . import views  # views renders the content
# views also handles the "POST" data
# can also redirect

urlpatterns = [
    # similar to app route in flask will send info to --> views
    url(r'^$', views.index),
    # This is the equivalent to blank index
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.number), ##
    url(r'^(?P<number>\d+)/edit$', views.number_edit),
    url(r'^(?P<number>\d+)/delete$', views.number_delete)
]

#url(r'^(?P<x>\d+)$', views.numbers)# this would work also
# this worked as well --> url(r'^/delete/(?P<number>\d+)$', views.number_delete)

# example num2 --> url(r'^(?P<number>\d+)$', views.number),
# url(r'^/edit/(?P<number>\d+)$',

#year can be done as  url(r'^(?P<year>[0-9]{4}/(?P<month>[09]{2}))/$', views.namegoeshere)
