# ParkingMeter.py
# 
# @ author: A. N. Other
# date: September 2016

print ("Kia Ora, this is the parking meter")
park_time = 4
print ("park_time time is ", park_time, "hours.")

rate = 4
cost = 0
if park_time > 3:
    cost = rate* 3
    # drop th erate by $2
    rate -= 2
    # get the remainder of the parking time
    park_time -= 3
    # add to the current cost
    cost += rate * park_time
    print("The cost of the parking is $", cost)
else:
    cost = rate * park_time
    print("The cost of the parking is $", cost)