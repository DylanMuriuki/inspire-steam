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
    #print(math.sin(x))
    #print(math.cos(x))
    #print(math.tan(x))

    print(f"The cosine of {x} is {math.cos(x)}")
    print(f"The sine of {x} is {math.sin(x)}")
    print(f"The tangent of {x} is {math.tan(x)}")

    