import calendar
print(calendar.weekheader(3))
print((calendar.firstweekday()))
print(calendar.month(2020, 4, w = 0, l = 0))
#print(calendar.monthcalendar(2020, 4))
#print(calendar.calendar(2020))
'''for i in range(1, 13):
    print(calendar.monthcalendar(2020, i))'''
print(calendar.weekday(2020, 4, 30))
print(calendar.isleap(2020))
print(calendar.leapdays(2000, 3000))
