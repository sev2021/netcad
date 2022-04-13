year = int(input("Enter a year: "))

#
# Write your code here.
#	

result = "Common year"
if year < 1582:
    result = "Not within the Gregorian calendar period"
else:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        result = "Leap year"

    
print(result) 
