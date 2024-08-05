#Exercise no 5 - To Check Wether given year is Leap year or Not using all the if&Else Function

year = int(input("Which year you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else: I
        print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

