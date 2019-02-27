""" There are naive and aware datetime
Naive: don't have time zones and daylight savings
"""

import datetime

# d = datetime.date(2018, 1, 24) # no zeros!!!
# print(d)

# tday = datetime.date.today()
# print(tday)

""" 
.weekday() Monday is 0 Sunday is 6
.isoweekday() Monday is 1 Sunday is 7
"""
tday = datetime.date.today()
# print(tday.isoweekday)

# Time Delta
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2019, 5, 26)
till_bday = bday - tday
print(till_bday)