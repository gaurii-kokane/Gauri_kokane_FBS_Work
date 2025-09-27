#Write a program to calculate area of circle 

import math
def areaCircle(radius):
    return math.pi * radius ** 2
r = float(input("Enter radius of circle: "))
print("Area of Circle =", areaCircle(r))


