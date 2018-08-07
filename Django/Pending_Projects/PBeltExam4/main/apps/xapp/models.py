from django.db import models
import bcrypt
from datetime import datetime
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import date

now = str(datetime.now())
# print(type(now))
today = str(date.today())
print(today)
print(now)

def ValidateEmail(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False

class UserManager(models.Manager):

    def regValidator(self, form):

        errors = []
        if not ValidateEmail(form['email']):
            errors.append("Email must have valid format.")
        elif User.objects.filter(email=form['email']):
             errors.append("Account already exists.")
        if len(form['name']) < 3:
            errors.append("Name must have at least 3 characters.")
        if len(form['username']) < 2:
            errors.append("Username must have at least 3 characters.")
        elif User.objects.filter(username=form['username']):
             errors.append("Username already exists.")
        if not form['bday']:
            errors.append('Date of Birth date is required.')
        elif form['bday'] > now:
            errors.append("Date of Birth date can't be in the future.")
        if len(form['pass']) < 5:
            errors.append("Password must have at least 5 characters.")
        elif form['pass'] != form['confirmpass']:
            errors.append("Password and confirm password must match.")

        if not errors:
            hash1 = bcrypt.hashpw(form['pass'].encode(), bcrypt.gensalt())
            user = User.objects.create(name=form['name'], username=form['username'], email=form['email'], bday=form['bday'], password=hash1)
            return (True, user)
        else:
            return (False, errors)

    def loginValidator(self, form):

        errors = []

        if not form['email']:
            errors.append("email required.")
        elif not User.objects.filter(email=form['email']):
             errors.append("Please register first")
        elif len(form['pass']) < 5:
            errors.append("Password must have at least 5 characters.")
        else:
            user = User.objects.filter(email=form['email'])
            if not bcrypt.checkpw(form['pass'].encode(), user[0].password.encode()):
                errors.append("Sorry, password does not match our records.")

        if not errors:
            return (True, user[0])
        else:
            return (False, errors)

class AppointmentValidator(models.Manager):

     def appointmentValidator(self, form, user_id):
        errors = []

        if not form['task']:
            errors.append('A task is required')
        if len(form['task']) < 4:
            errors.append('Task name needs to be more than 3 characters')
        if not form['date']:
            errors.append('Task date is required.')
        elif form['date'] < today:
            errors.append("Task needs to be in the future.")
        if not form['hour']:
            errors.append('Hour date is required.')
            
        if not errors:
            client = User.objects.get(id=user_id)
            appointment = Appointment.objects.create(task=form['task'],hour=form['hour'],date=form['date'], client=client)   

            return (True, appointment)
        else:
            return (False, errors)


class User(models.Model):
    name = models.CharField(max_length=15)
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=15) 
    bday = models.DateTimeField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)  
   

    # joins (connets our Trip model with out User model through our Join table)
    # trips (connects our Trip model with our User model (Trip table)
    def __repr__(self):
        return "<User {} | {} | {} {}>".format(self.id, self.name, self.username, self.email)

    objects = UserManager()

class Appointment(models.Model):
    task = models.CharField(max_length=10)
    hour = models.TimeField()
    date = models.DateTimeField()
    status = models.CharField(max_length=10, default='Pending')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    client = models.ForeignKey(User, related_name="bookings")

   
    def __repr__(self):
        return "<Appointment {} | {} | {} {}>".format(self.id, self.task, self.hour, self.client) 
        
    objects = AppointmentValidator()


