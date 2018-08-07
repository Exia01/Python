rom django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bcrypt
#2
# Create your models here.
# email validator
def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False
#3
# Registration Validator
class UserManager(models.Manager):
    def regValidator(self, form):
        errors = []

        if len(form['fname']) < 3:
            errors.append("First name must be at least 3 characters long.")
        if len(form['lname']) < 3:
            errors.append("Last name must be at least 3 characters.")
        if not form['email']:
            errors.append("Email Required")
        elif not ValidateEmail(form['email']):
            errors.append("Email must have a valid format!")
        elif User.objects.filter(email=form['email']):
            errors.append("Account already exists.")
        if len(form['password']) < 5:
            errors.append("Password must at least have 5 characters!")

        if len(errors) == 0:
            hash1 = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(fname=form['fname'], lname=form['lname'], email=form['email'], password=hash1)
            return (True, user)
        else:
            return (False, errors)

    def loginValidator(self, form):
        errors = []
        if not form['email']:
            errors.append("Email is required")
        if not form['password']:
            errors.append("Password is required")
        elif not ValidateEmail(form['email']):
            errors.append("email must have a valid format.")
        elif not User.objects.filter(email=form['email']):
            errors.append("Please register first")
        
        elif len(form['password']) < 5:
            errors.append("Password must have at least 5 characters.")
        else:
            user = User.objects.filter(email=form['email'])
            if not bcrypt.checkpw(form['password'].encode(),user[0].password.encode()):
                errors.append("Password does not match password in database.")

        if not errors:
            return (True, user[0])
        else:
            return (False,errors)
#1
class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return "<User {}| {} {}| {}".format(self.id, self.fname, self.lname, self.email)

    objects = UserManager()

class Items(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey("User", related_name = "creator")
    adder = models.ManyToManyField("User", related_name = "adder")

