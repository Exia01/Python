from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __repr__(self):
        return "<User: {}|{} {} {}>".format(self.id, self.fname, self.lname, self.email)