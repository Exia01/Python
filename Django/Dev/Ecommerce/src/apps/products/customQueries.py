"""
These are custom query sets that can then by used by the model manager

Similar to respository and service in Java?

Similar to Controller and Service in MEAN?

"""
from django.db import models

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        self.filter(featured=True, active=True)

    def active(self):
        self.filter(active=True)
