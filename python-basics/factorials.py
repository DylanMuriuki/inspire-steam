#Name:Dylan Muriuki
#Date:16/02/2026
#Program to calculate the factorials of numbers

#x!=x factorial

factorial=1
number=int(input("Enter the number x:"))
#Initialise factorial as 1

for x in range(1,number+1):
    factorial*=x

print(f"Factorial of {number} is {factorial}")