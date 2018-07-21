# you can write to stdout for debugging purposes, e.g.
# print(("this is a debug message"))
import datetime
def solution(Y, A, B, W):
    # write your code in Python 3.6
    
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    start_momth = months[A]
    #print ("start_momth", start_momth)
    end_month = months[B]
    #print ("end_month", end_month)
    week_day = {"Sunday":6, "Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5}
    start_day = week_day[W]
    d = datetime.date(Y,start_momth, start_day)
    next_monday = next_weekday(d, 0)
    #print ("mon",next_monday)
    d = datetime.date(Y,end_month, 1)
    last_sunday = last_day(d, 6)
    
    #print ("sun",last_sunday.day)
    
    start_month_days = days[start_momth-1]
    #print(start_month_days)
    last_month_days = days[end_month-1]
    #print(last_month_days)
    
    #print((start_month_days - next_monday.day)//7)
    #print(last_sunday.day//7)
    if start_month_days - next_monday.day == 0:
        vacation = (start_month_days - next_monday.day)//7 + (last_sunday.day//7)
    else:
        vacation = (start_month_days - next_monday.day)//7 + 1 + (last_sunday.day//7)
    return vacation 
        

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    #print(("->", d.weekday()))
    if days_ahead <= 7: 
        days_ahead += 7
    
    return d + datetime.timedelta(days_ahead)
    
def last_day(d, weekday):
    days_ahead = weekday - d.weekday()
    #print(("->", d.weekday()))
    if days_ahead <= 21: # Target day already happened this week
        days_ahead += 21
        
    return d + datetime.timedelta(days_ahead)


print (solution(2014, "April", "May", "Wednesday"))


    