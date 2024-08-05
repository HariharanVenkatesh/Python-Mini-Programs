#Excersice no 16 - Prime number checker

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