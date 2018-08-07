from __future__ import unicode_literals
from django.db import models
from  django.core.validators import validate_email
from django.core.exceptions import ValidationError


def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class OwnerManager(models.Manager):

    # form is the req.POST dictionary
    def validator(self, form):
        errors = []

        # if len(form['fname']) <1:
        if not form['fname']:
            errors.append("First name is required.")
        if not form['lname']:
            errors.append("Last name is required.")
        if not form['email']:
            errors.append("Email is required.")
        elif not ValidateEmail(form['email']):
            errors.append("Must be valid email format.")

        if not errors:
            owner = Owner.objects.create(fname=form['fname'], lname=form['lname'], email=form['email'])
            return (True, owner)
        else:
            return (False, errors)






class Owner(models.Model):
    fname = models.CharField(max_length = 255)
    lname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<Owner: {}|{} {}>".format(self.id, self.fname, self.email)

    objects = OwnerManager()




class Pet(models.Model):
    name = models.CharField(max_length = 255)
    breed = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey(Owner, related_name="pets")

    def __repr__(self):
        return "<Pet: {}|{} {}>".format(self.id, self.name, self.breed)
