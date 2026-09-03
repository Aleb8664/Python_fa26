"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Ask user for Monthly Income (float).
[X] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[X] 4. Calculate Total Expenses and Remaining Balance.
[X] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# This is the introduction to the program, this lets the user know what they are doing!
print("\n\nHello user, To begin I (the program) is going to ask a few questions.\n")


# This section is the round of questioning for the user to find out how  much they make, their spending and the amount they would like to save
user_name = input("Please enter your name:  ")
print(f"thank you {user_name}!\n")
income_monthly = float(input("Please State your monthly income:  "))
print(f"{user_name}, You entered ${income_monthly:,.2f} as your monthly income!\n")
car_monthly = float(input("Please enter your monthly car payment and repair cost:  "))
print(f"{user_name}, You entered ${car_monthly:,.2f}!\n")
rent_monthly = float(input("please enter your monthly rent:  "))
print(f"{user_name} you entered ${rent_monthly:,.2f}!\n")
electric_monthly = float(input("Please enter your monthly electric bill:  "))
print(f"{user_name}, You entered ${electric_monthly:,.2f}!\n")
water_monthly = float(input("Please enter your monthly water bill:  "))
print(f"{user_name}, You entered ${water_monthly:,.2f}!\n")
internet_monthly = float(input("Please enter your monthly home internet bill:  "))
print(f"{user_name}, You entered ${internet_monthly:,.2f}!\n")
cell_monthly = float(input("Please enter your monthly Cellphone bill:  "))
print(f"{user_name}, You entered ${cell_monthly:,.2f}!\n")
subscriptions_monthly = float(
    input(
        "Please enter your monthly spending on subscription services Netflix, Youtube, Cable tv, ETC..:  "
    )
)
print(f"{user_name}, You entered ${subscriptions_monthly:,.2f}!\n")
other_monthly = float(input("Please enter any other monthly spending:  "))
print(f"{user_name}, You entered ${other_monthly:,.2f}!\n")
print(
    "Congratulations the questioning is now over, some calculations will be made and displayed below \n"
)

# this section will be the calculations
expenses = (
    car_monthly
    + rent_monthly
    + electric_monthly
    + water_monthly
    + internet_monthly
    + cell_monthly
    + subscriptions_monthly
    + other_monthly
)
print(f"expenses: ${expenses:,.2}!")

remaining_balance = income_monthly - expenses
print(f"remaining balance: ${remaining_balance:,.2}!")

percentage_spent = expenses / income_monthly
print(f"Percentage spent: {percentage_spent:,.2%}!")

# Formatter to fix gaps in the table eg when using the print statement with the allignment options it would output $     400 instead of $400 (is there a better way of doing this probobally)
formatter_car
formatter_electric
Formatter_


# this will be the output
print(f"{'Rent':<20} ${rent_monthly:>10,.2f}")
