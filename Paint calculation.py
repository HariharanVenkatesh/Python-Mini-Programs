#Excersice no 15 - Paint calculation

import math
def paint_calculation(Height,Width,Cover):
    Area = Height * Width
    no_of_cans = math.ceil(Area/Cover)
    print(f"You will need {no_of_cans} Cans of Paint.")
H = int(input("Enter the Height of wall in meters: "))
W = int(input("Enter the Width of wall in meters: "))
coverage = 7
paint_calculation(Width = W,Height = H,Cover = coverage)