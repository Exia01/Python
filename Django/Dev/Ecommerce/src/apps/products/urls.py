from django.conf.urls import url
from .views import (
    ProductListView,
    # ProductDetailView,
    ProductDetailSlugView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    )


urlpatterns = [  # naming space for easier method
    url(r'^$', ProductListView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$',ProductDetailView.as_view(), name='details'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^featured$', ProductFeaturedListView.as_view(), name='featured'),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name='details'),
    # url(r'^(?P<pk>\d+)/$', product_detail_view, name='details'),
]
