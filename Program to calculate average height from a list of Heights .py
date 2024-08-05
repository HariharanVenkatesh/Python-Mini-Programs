#Excersice no -11 Program to calculate average height from a list of Heights 

heights = input("Enter Heights Seperated by space: ")
height_list = heights.split()
count = 0
for height in height_list:
    count = count + 1
print(count)
for i in range(count):
    height_list[i] = int(height_list[i])
total = 0
for person in height_list:
    total += person
avg = total/count
print("Average height is :",round(avg))           
