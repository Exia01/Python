from django.conf.urls import url
from .views import (
    ProductListView,
    ProductDetailSlugView,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
    )


urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    # ## Unused routes. May implement later 
    # url(r'^(?P<pk>\d+)/$',ProductDetailView.as_view(), name='details'),
    # url(r'^featured$', ProductFeaturedListView.as_view(), name='featured'),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name='details'),
    # url(r'^(?P<pk>\d+)/$', product_detail_view, name='details'),
]
