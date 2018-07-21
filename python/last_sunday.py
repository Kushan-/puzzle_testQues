import datetime
def next_weekday(d, weekday): 
   days_ahead = weekday - d.weekday()
    print("->", d.weekday())
    if days_ahead <= 21: # Target day already happened this week
        days_ahead += 21
        
    return d + datetime.timedelta(days_ahead)

d = datetime.date(2018,5, 1)
print(d)
next_monday = next_weekday(d, 6) # 0 = Monday, 1=Tuesday, 2=Wednesday...
print("sun->", next_monday)







#http://code.activestate.com/recipes/425607-findng-the-xth-day-in-a-month/
