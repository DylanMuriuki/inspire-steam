#Name:Dylan Muriuki
#Date:16/02/2026
#Program to calculate income tax

salary=int(input("Enter your gross salary:"))

if salary < 50000:
    tax = (2.5 * salary)/100
    net_salary = salary - tax
print(f"The gross salary is:{salary}")
print(f"The net salary is:{net_salary}")
print(f"The tax paid is:{tax}")