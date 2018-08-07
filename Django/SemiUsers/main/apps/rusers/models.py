from __future__ import unicode_literals
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class UserManager(models.Manager):
    def validator(self, form):
        errors = {}
        if len(form['fname']) < 3:
            errors['fname'] = "First Name needs to have at least 3 characters!"
        if len(form['lname']) < 3:
            errors['lname'] = "Last Name needs to have at least 3 characters!"
        if len(form['email']) < 3:
            errors['email'] = "Name needs to have at least 3 characters!"
        return errors


class User(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    def __repr__(self):
        return "<User: {}|{} {} {} {}>".format(self.id, self.fname, self.lname, self.email, self.created_at)
