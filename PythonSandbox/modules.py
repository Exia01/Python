# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime 
from datetime import date
# Above, just bringing in the datetime 
import time
from time import time

# Pip modules

# import camelcase # --> imports camelcase

# Custom modules
import validator
# we can also import just the validate_email
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

# camel = camelcase.CamelCase()
text = 'hello there world'
# print(camel.hump(text))

# Custom modules

email = 'test@test.com'
if validate_email(email):
  print('Email is valid')
else:
  print('Not an email')