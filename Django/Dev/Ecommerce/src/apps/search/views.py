from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from ..products.models import Product

class SearchProductView(ListView):
    template_name = 'search/view.html'
    # using instead request.GET.q
    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context 

    def get_queryset(self, *args, **kwargs):
        request = self.request
        # print(request.GET)
        dict = request.GET
        query = request.GET.get('q', None) # dict method "get"
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()




"""
__icontains = field contains this 
__iexact = field is exact
"""