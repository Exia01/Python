from django.conf.urls import url
from . import views  # views renders the content
# views also handles the "POST" data
# can also redirect

urlpatterns = [
    # similar to app route in flask will send info to --> views
    url(r'^$', views.index),
    url(r'^lecture$', views.index),
    url(r'^blog$', views.blog),
    url(r'^blog/create$', views.create),
    url(r'^time_display$', views.timenow),
    url(r'^word_generator$', views.wordnow),
    url(r'^generate$', views.generate)
    # url(r'^lecture',('apps.lecture.urls')),
    # This is the equivalent to blank index
]
    
# this worked as well --> url(r'^/delete/(?P<number>\d+)$', views.number_delete)

# example num2 --> url(r'^(?P<number>\d+)$', views.number),
# url(r'^/edit/(?P<number>\d+)$',

#year can be done as  url(r'^(?P<year>[0-9]{4}/(?P<month>[09]{2}))/$', views.namegoeshere)