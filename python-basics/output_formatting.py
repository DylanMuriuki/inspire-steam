#Name:Dylan Muriuki
#Date:17/02/2026
#Program to format the output in different styles

name="Dylan Muriuki" #name

weight= 72 #weight in kgs

favourite_team= "Arsenal"

height= 126.86 #height in cm

#1.Format using print(f"{}")
print(f"My name is {name} and I weigh {weight}kgs.")

#2.Format using f string
fstring=f"My name is {name} and I support {favourite_team}."
print(fstring)

#3.Format using {} and .format
print("My name is {0} and I am {1}cm tall.".format(name,height))

#4.Format using output specifiers %s
import math
print("The value of pi is approximately %5.3f."%math.pi)
print("I favourite team is %s and I weigh %skgs."%(favourite_team,weight))