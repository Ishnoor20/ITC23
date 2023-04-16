# Ask the user for their gross income and number of dependents
gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents you have: "))

# Compute the taxable income and tax amount
standard_deduction = 10000
dependent_deduction = 3000
taxable_income = gross_income - standard_deduction - (dependent_deduction * num_dependents)
tax_rate = 0.20
income_tax = taxable_income * tax_rate

# Print the results
print(f"Your taxable income is ${taxable_income:.2f}")
print(f"Your income tax is ${income_tax:.2f}")
