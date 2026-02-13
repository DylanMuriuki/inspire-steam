#Name:Dylan Muriuki
#Date:13/02/2026
#Program to calculate geometric progression

#Calculating the nth term

a=int(input("Enter the first number:"))
r=int(input("Enter the common ratio:"))
n=int(input("Enter the number of terms :"))

nth_term=(a*(r**(n-1)))
print(f"The nth term is:{nth_term}")

#Calculating the sum of a geometric progression

Sn=(a*(1-(r**n)))/(1-r)
print(f"The sum of the geometric progression is:{Sn}")

sn=(a*((r**n)-1))/(r-1)
print(f"The sum of the geometric progression is:{sn}")