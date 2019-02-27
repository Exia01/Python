import datetime
import pytz

dt_eastern = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))

print(dt_eastern.strftime('%B %d, %Y'))  # full month, 2 digit day, full year

dt_str = 'February 01, 2019'  # string --> string operation
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)


# strftime - Datetime to string
# strptime - String to Datetime