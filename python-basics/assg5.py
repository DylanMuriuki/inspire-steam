#Name:Dylan Muriuki
#Date:16/02/2026
#Program to calculate income tax

salary=int(input("Enter your gross salary:"))

if salary < 50000:
    tax = (2.5 * salary)/100

elif 100000 > salary >= 50000:
    tax = (4.5 * salary)/100
    
else:
    salary >= 100000
    tax = (7.5 * salary)/100

net_salary=salary-tax
print(f"The gross salary is:{salary}")
print(f"The tax paid is:{tax}")
print(f"The net salary is:{net_salary}")
  