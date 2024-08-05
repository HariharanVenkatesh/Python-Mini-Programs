#Excersice no 20 - Circle excercise using oop concepts like Attributes and Methods

class circle:
    pi = 3.14      #Class Object attribute
    def __init__(self,radius):
        self.radius = radius
    def get_circumference(self):
       return 2 *self.pi *self.radius
circle_1 = circle(4)
print(circle_1.get_circumference())

class circle:
    pi = 3.14      #Class Object attribute
    def __init__(self,radius = 7):
        self.radius = radius
        self.area = circle.pi * radius *radius
    def get_circumference(self):
    #    return 2 *self.pi *self.radius
        return 2 * circle.pi *self.radius
circle_1 = circle(4)
print (f"The circumference of Circle 1 is: {circle_1.get_circumference()}")
circle_2 = circle(14)
print (f"The circumference of Circle 2 is: {circle_2.get_circumference()}")
print (f"The area of circle 1 is: {circle_1. area}")    
# circle_1 = circle(8)                       
# print(circle_1.get_circumferance())
# circle_2 = circle(14)
# print(circle_2.get_circumferance())
# print(circle_1.area)    
