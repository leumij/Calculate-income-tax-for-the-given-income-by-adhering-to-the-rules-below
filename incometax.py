# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

# Pseudocode
# Ask user for Total income
total_income = int(input("please introduce your total income: "))

# Solve for income tax
first = int(10000) * float(0.0)
second = int(10000) * float(0.1)
remain = total_income - int(20000)
final = remain * float(0.2)
total_tax = first + second + final


