from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt


def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []

        if len(form['fname']) < 3:
            errors.append("First name must be at least 3 characters.")
        if len(form['lname']) < 3:
            errors.append("Last name must be at least 3 characters.")
        if not form['email']:
            errors.append("Email is required.")
        elif not ValidateEmail(form['email']):
            errors.append("Email must have valid format.")
        elif User.objects.filter(email=form['email']):
            errors.append("Sorry, account already exists.")
        if len(form['pass']) < 5:
            errors.append("Password must have at least 5 characters.")

        if len(errors) == 0:
            hash1 = bcrypt.hashpw(form['pass'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                fname=form['fname'], lname=form['lname'], email=form['email'], password=hash1)
            return (True, user)
        else:
            return (False, errors)

    def loginValidator(self, form):

        errors = []

        if not form['email']:
            errors.append('Email is required.')
        elif not ValidateEmail(form['email']):
            errors.append('Email must have a valid format')
        elif not User.objects.filter(email=form['email']):
             errors.append("Please register first")
        elif len(form['pass']) < 5:
            errors.append("Password must have at least 5 characters.")
        else:
            user = User.objects.filter(email=form['email'])
            if not bcrypt.checkpw(form['pass'].encode(), user[0].password.encode()):
                errors.append("Password does not match record.")

        if not errors:
            return (True, user[0])
        else:
            return (False, errors)


class User(models.Model):
    fname = models.fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User {}| {} {} | {}".format(self.id, self.fname, self.lname, self.email)

    objects = UserManager()
