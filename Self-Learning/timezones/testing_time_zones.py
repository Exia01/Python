import datetime
import pytz

dt = datetime.datetime(2016, 7, 8, 11, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC) 
print(dt_now)
 #both print utc but not localized

# same as dt_now
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow) #current utcnow but not offset

dt_eastern = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print(dt_eastern) # this is offset

# for tz in pytz.all_timezones: # this will list out all timezones
#     print(tz)

""" Making a naive datetime timezone aware """

dt_eastern = datetime.datetime.now() # naive / no timezone
eastern_tz = pytz.timezone('US/Eastern')
print(dt_eastern)

dt_eastern = eastern_tz.localize(dt_eastern)  # made a naive timzone aware
dt_pacific = dt_eastern.astimezone(pytz.timezone('US/Pacific')) # coverted
print(dt_eastern)
print(dt_pacific)
