#Name:Dylan Muriuki
#Date:17/02/2026
#Program to display a diamond

rows = int(input("Enter number of rows: "))

# Upper part of diamond
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower part of diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

#Program to display a triangle

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))
