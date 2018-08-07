from __future__ import unicode_literals
from django.db import models



class Owner(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()                              # It should be noted that you never want to store age. That is because you would have to update it every year.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owners = models.ManyToManyField(Owner,on_delete=models.CASCADE, related_name="pets")


# One to Many
# Order Matters in One to Many.

class Owner(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pet(models.Model):
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.IntegerField()                              # It should be noted that you never want to store age. That is because you would have to update it every year.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owners = models.ForeignKey(Owner, related_name='pets')


# After creating these Classes you need to migrate. Migration is akin to forward engineering in MySQL Workbench


# To Import Models In Command line

#python python manage.py shell
#under Main 
# from apps.my_app.models import Owner
# from apps.my_apps.models import Pet
# Owner.objects.all()
# To create
# Owner.objects.create(fname="Meggie", lname="Chen")
# User.objects.create(fname="John", lname="Doe")
# terminal replies     <Owner: Owner object>
# That terminal reply is not useful so why not create a method to display the names
# This method is called the reaper method to display the data.


def __repr__(self):
    return "<Owner: {}|{} {}>".format(self.id, self.fname, self.lname)


# lets create one for pets


def __repr__(self):
    return "<Pet: {}|{} {}>".format(self.id, self.name, self.breed)


# python manage.py make migrations
# python manage.py make migrate
