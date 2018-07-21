def is_leap_year(year):
    """Determine whether a year is a leap year."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


import calendar
print calendar.isleap(2020)

print is_leap_year(2020)



from datetime import date
from datetime import timedelta

today = date.today()
print today
print "weekday->",today.weekday()
offset = (today.weekday() - 2) % 7
print "off->",offset
print timedelta(days=offset)
last_wednesday = today - timedelta(days=offset)

print last_wednesday
