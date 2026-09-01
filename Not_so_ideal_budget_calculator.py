"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

print("Hello user, To begin I (the program) is going to ask a few questions.\n")

user_name = input("Please enter your name:  ")
print(f"thank you {user_name}!\n")
income_monthly = float(input("Please State your monthly income:  "))
print(f"{user_name}, You entered ${income_monthly:,.2f} as your monthly income!\n")
