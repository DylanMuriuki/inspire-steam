#Name:Dylan Muriuki
#Date:15/02/2026

#Program for get the square of numbers

x=int(input("Enter the number:"))

sq_x=x**2
print(f"The square of {x} is {sq_x}")


#Program to perform trigonometric functions

import math

for x in range(-180,180,30):
    print(x)
    print(math.sin(x))
    print(math.cos(x))
    print(math.tan(x))


#Program to calculate geometric progression

a=int(input("Enter the first number:"))
r=int(input("Enter the common ratio:"))
n=int(input("Enter the number of terms:"))

nth_term=(a*(r**(n-1)))
print(f"The nth term is:{nth_term}")