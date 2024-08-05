#Excercise no 9 -To Which will select a random name from a list of names&the person selected will have to pay for everybody's food bill

import random
names = input("Enter everybody's name separated by comma: ")
names_list = names.split(",")
print(names_list)
Length = len (names_list)
random_choice = random.randint(0, Length-1)
Person_Selected = random.choice (names_list)
print (f" {random.choice (names_list)} will pay the bill")

