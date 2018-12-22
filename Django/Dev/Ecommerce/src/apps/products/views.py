from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()  # all queryset
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     return context # get the context for whatever view is being done


# function based views
def Product_List_View(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "product/product_list_view.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()  # all queryset
    template_name = 'products/detail.html'

    # def get_context_data(self, *args, **kwargs): #automatically separating the data
    #     context = super().get_context_data(*args, **kwargs)
    #     print(context)
    #     return context # get the context for whatever view is being done


# def product_detail_view(request, pk=None, *args, **kwargs):
#     instance = Product.objects.get(pk=pk, featured=True)  # id #instace as object
#     instance = get_object_or_404(Product, pk=pk, featured=True)
#     try:
#         instance = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         print('no product here')
#         raise Http404("Product doesn't exist")
#     except:
#         print("huh?")

#     instance = Product.objects.get_by_id(pk)
#     if instance is None:
#         raise Http404("Product doesn't exist")
#     print(instance)
#     qs = Product.objects.filter(id=pk)

#     # print(qs)
#     if qs.exists() and qs.count() == 1:  # len(qs)
#         instance = qs.first()
#     else:
#         raise Http404("Product doesn't exist")

#     context = {
#         'object': instance
#     }
#     return render(request, "products/detail.html", context)
