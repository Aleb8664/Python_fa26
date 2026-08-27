"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS (DO NOT DELETE)
-----------------------------------------------------------------------
[*] 1. Header Docstring included.   (is this is the header?)
[*] 2. Define a String variable.
[*] 3. Define an Integer variable.
[*] 4. Define a Float variable.
[*] 5. Define a Boolean variable.
[*] 6. Print all variables using F-Strings.
[*] 7. Upload to GitHub.
-----------------------------------------------------------------------
"""

item_name = "apple"  # string
item_type = "food"  # string
item_amount = 4  # integer
item_value = 0.5  # float/decimal
item_can_heal = True  # boolean
item_health_restore = 10  # integer

print(
    f" Item selected: {item_name} \n Item Type: {item_type} \n Quantity: {item_amount} \n Value: ${item_value} \n Health item: {item_can_heal} \n Health restore: {item_health_restore} hp"
)  # F-string statement showing the item you have selected in the inventory
