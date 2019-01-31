import datetime  # does not have timezone information

t = datetime.time(9, 30, 45, 100000)  # hours minutes seconds microseconds 
print(t)

dt = datetime.datetime(2018, 7, 12, 2, 30, 15, 100000)
print(dt)  #year month day plus time)

tdelta = datetime.timedelta(days=7) #can even do hours 
print(dt + tdelta)  # adds a week


# Constructors
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow() # not aware time because of having to add tz

print(dt_today)
print(dt_now)
print(dt_utcnow)