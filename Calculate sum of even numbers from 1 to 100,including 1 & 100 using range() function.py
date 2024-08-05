#Excersice no 13 - Calculate sum of even numbers from 1 to 100,including 1 & 100 using range() function

sum =0
for i in range(1,101):
    if i % 2 == 0:
        sum += i
print(sum)