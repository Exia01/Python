from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product


class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()  # all queryset
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):  # using instead of queryset in ln 9
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()  # all queryset
    template_name = 'products/featured-detail.html'

    def get_queryset(self, *args, **kwargs):  # using instead of queryset in ln 9
        request = self.request
        print('from details featured', Product.objects.featured())
        return Product.objects.featured()



class ProductFeaturedListView(ListView):
    # queryset = Product.objects.all()  # all queryset
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):  # using instead of queryset in ln 9
        request = self.request
        return Product.objects.all()


class ProductListView(ListView):
    # queryset = Product.objects.all()  # all queryset
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     return context # get the context for whatever view is being done

    def get_queryset(self, *args, **kwargs):  # usingh instead of queryset in ln 9
        request = self.request
        return Product.objects.all()


# function based views
def Product_List_View(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "product/product_list_view.html", context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()  # all queryset
    template_name = 'products/detail.html'

    # def get_context_data(self, *args, **kwargs): #automatically separating the data
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     return context # get the context for whatever view is being done

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        print(instance)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):  # using instead of queryset in ln 9
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk, featured=True)  # id #instace as object
    # instance = get_object_or_404(Product, pk=pk, featured=True)

    #  ## Using try Method
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")
    # ##Using Custom Model Manager
    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product doesn't exist")

    # # ## -> using IF and else queryset
    # qs = Product.objects.filter(id=pk)

    # # print(qs)
    # if qs.exists() and qs.count() == 1:  # qs has a property as a count which more efficient in dbs
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
