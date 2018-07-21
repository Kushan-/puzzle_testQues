import datetime
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    print("->", d.weekday())
    if days_ahead <= 7: # Target day already happened this week
        days_ahead += 7
        
    return d + datetime.timedelta(days_ahead)

d = datetime.date(2018,11, 1)
print(d)
next_monday = next_weekday(d, 0) # 0 = Monday, 1=Tuesday, 2=Wednesday...
print("mon->", next_monday)







#http://code.activestate.com/recipes/425607-findng-the-xth-day-in-a-month/
