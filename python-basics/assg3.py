#Name:Dylan Muriuki
#Date:15/02/2026
#Program to perform trigonometric functions

import math

#Trigonometry functions table
#Sin/Cos/Tan angles

#print(f"The cos of {x} is {math.cos(x)}")
#print(f"The sine of {x} is {math.sin(x)}")
#print(f"The tangent of {x} is {math.tan(x)}")
#Header

print(" Angle              Sin                   Cos                    Tan ")
print("-"*80)

for x in range(-180,180,30):
    print(f"{x}         {math.sin(x)}    {math.cos(x)}     {math.tan(x)}  ") 