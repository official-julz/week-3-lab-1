#  import the 'calender' module
import calendar

# prompt th euser to input the year and month
y = int(input("Input the year :"))
m = int(input("Input the month :"))

# print the calender for the specified year and month
print(calendar.month(y,m))