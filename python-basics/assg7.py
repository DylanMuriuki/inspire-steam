#Name:Dylan Muriuki
#Date:17/02/2026
#Program to solve quadratic equations

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

#Formula
# x=-b + or - math.sqrt(b*b-4ac)/2a

#Discriminant
d = b*b - 4*a*c

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two real roots:", x1, "and", x2)

elif d == 0:
    x = -b / (2*a)
    print("One real root:", x)

else:
    print("No real roots")

