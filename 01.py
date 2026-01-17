# Write a Python program to display the current date and time.
import datetime

now = datetime.datetime.now()
print("date and time now is:",now)
print("year",now.year)
print("month",now.month)
print("day",now.day)
print("hour",now.hour)
print("min",now.minute)
print("sec",now.second)