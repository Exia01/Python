"""
These are custom query sets that can then by used by the model manager

Similar to respository and service in Java?

Similar to Controller and Service in MEAN?

"""
from django.db.models import Q
from django.db import models


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        tags=()
        lookups = (Q(title__icontains=query) | Q(description__icontains=query) | Q(
            price__icontains=query))  # sets a tuple?
        # Q(tag__name__icontains=query)
        return self.filter(lookups).distinct()
