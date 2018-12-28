from django.conf.urls import url
from .views import (
    SearchProductView,
  
    )


urlpatterns = [
    url(r'^$', SearchProductView.as_view(), name='query'),
    # ## Unused routes. May implement later 
    # url(r'^(?P<pk>\d+)/$',ProductDetailView.as_view(), name='details'),
    # url(r'^featured$', ProductFeaturedListView.as_view(), name='featured'),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name='details'),
    # url(r'^(?P<pk>\d+)/$', product_detail_view, name='details'),
]
