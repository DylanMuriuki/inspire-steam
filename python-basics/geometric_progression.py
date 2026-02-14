#Name:Dylan Muriuki
#Date:14/02/2026
#Program to calculate geometric progression

#Calculating the nth term
#Inputs are integers only

a=int(input("Enter the first number:"))
r=int(input("Enter the common ratio:"))
n=int(input("Enter the number of terms:"))

nth_term=(a*(r**(n-1)))
print(f"The nth term is:{nth_term}")

#Calculating the sum of a geometric progression

def geometric_sum(a,r,n):
    if r<1:
        #Formula:Sn=a(1-r^n)/(1-r)
        Sn=a*(1-r**n)/(1-r)

    elif r>1:
        #Formula:Sn=a(r^n-1)/(r-1)
        Sn=a*(r**n-1)/(r-1)
    
    else:
        #r==1
        #Formula:Sn=a*n
        Sn=a*n

    return Sn

answer=geometric_sum(a,r,n)

print("The sum of the geometric progression is",answer)