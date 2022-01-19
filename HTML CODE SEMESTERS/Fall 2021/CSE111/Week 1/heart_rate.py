"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum.
"""

import math

# calcualtes the optimal heart rate using age inputed
age = int(input("Please enter your age: "))
maxRate = (220 - age)
optimalLow = str(round(maxRate * .65)) + " "
optimalHigh = str(round(maxRate * .85)) + " "

print("When you exercise to strengthen your heart, you should keep your heart rate between " + optimalLow + "and " + optimalHigh + "beats per minute.")