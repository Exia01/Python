from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product


class ProductListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):  # using instead of queryset in ln 9
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    queryset = Product.objects.all()  # all queryset
    template_name = 'products/detail.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     return context  # get the context for whatever view is being done
    

class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()  # all queryset
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):  # using instead of queryset in ln 9
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()  # all queryset
    template_name = 'products/featured-detail.html'

def product_detail_view(request, pk=None, *args, **kwargs):

    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
