#Excersice no 16 - Prime number checker
#Ex 1:
import math
def prime_no_checker(Number):
    is_prime = True
    if Number == 1:
        is_prime = False
    for i in range(2,math.ceil(Number/2)+1):
        if Number % i == 0:
                is_prime == False
    if is_prime:
        print("It is a Prime Number")
    else:
        print("Not a Prime Number")
N = int(input("Enter a number: "))
prime_no_checker(N)            

#Ex 2:
import math
def prime_checker(number):
    is_prime = True
    for i in range(2,math.ceil(math.sqrt(n))):
        if number % i == 0:
            is_prime = False
    if number == 1:
        print(f"{number} is neither prime nor composite")
    elif is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is a composite number")
n = int(input("Enter a number: \n"))
prime_checker(n)
