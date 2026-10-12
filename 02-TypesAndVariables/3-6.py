###Program for measuring the distance to the horizon

import math

h = float(input("Enter height of the observer in meters: "))
d = 3.57 * math.sqrt(h)
print("Distance to the horizon in kilometers is: ", d)