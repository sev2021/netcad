# Write and test a function which takes three arguments 
# (a year, a month, and a day of the month) 
# and returns the corresponding day of the year.

def is_year_leap(year):
    return bool(year % 400 == 0 or year % 4 == 0 and year % 100)


def days_in_month(year, month):
    months_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        months_arr[1] = 29
    return months_arr[month - 1]
    

def day_of_year(year, month, day):
    return sum( days_in_month(year, m + 1) for m in range(month - 1) ) + day


print(day_of_year(2000, 12, 31))
