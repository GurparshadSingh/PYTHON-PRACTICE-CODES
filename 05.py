# Write a Python program to print the calendar of a given month and year.
import calendar
month = int(input("Enter month"))
year = int(input("Enter year"))

if month < 1 or month > 12:
    print("invalid month ")
else:
    print("calendar of given month and year is",calendar.month(year,month))


