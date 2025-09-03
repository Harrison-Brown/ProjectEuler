'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"] #month, display use only
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #how many days are in 

dayOfWeek = 1 # Sunday is 0
listOfSundays = []
sundays = 0
date = 1
month = 0 # January is 0
year = 1900

while year < 2001:
    if year % 4 == 0 and year != 1900:
        days[1] = 29
    else:
        days[1] = 28
    date += 1
    dayOfWeek = (dayOfWeek + 1) % 7
    if date > days[month]:
        month += 1
        date = 1
    if month > 11: # month 0 is january
        year += 1
        month = 0
    if dayOfWeek == 0:
        sundays += 1
        string = "{} {}, {}".format(months[month], date, year)
        if year > 1900 and year < 2001 and date == 1 and dayOfWeek == 0:
            sundays += 1
            print("**{}".format(string)) #debug
            listOfSundays.append(string)
        else:
            print(string) #debug
        
# SOLUTION: 171