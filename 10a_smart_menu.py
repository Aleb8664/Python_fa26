"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = [
    "peperoni",
    "cheese",
    "sausage",
    "bacon",
    "pineapple",
    "ham",
    "olives",
    "onion",
    "peppers",
]


def make_pizza(customer, size, topping, is_delivery=False):
    pass


def customer_info():
    pass


def sizes():
    pass


def topping():
    pass


def delivery():
    # reccursion loop, function calls itself when there is an error so the user can fix the mistake. in this case the user is asked to make a selection using an integer value, if the user inputs somethig else the the program will spit out an exception and call the functuion again.
    try:
        is_delivery = int(
            input(
                "will this yummy pizza be picked up or delivered?\n 1. Delivery ($5 charge)\n 2. Pickup ($free)\n Please enter numerical value:  "
            )
        )
        if is_delivery == 1:
            delivery = True
        elif is_delivery == 2:
            delivery == False
        else:
            print("ERROR NOT A VALID ANSWER pick 1 or 2")
            delivery()
        print(is_delivery)
    except Exception as e:
        print(f"ERROR!! {e} PLEASE ENTER NUMERICAL VALUE!")
        delivery()


def main():
    print("Aleb's Pizza ordering system")
    start_question = input("Would you like to order a Pizza? (Yes/No):  ").lower()
    print(start_question)
    if start_question == "yes" or start_question == "y":
        delivery()
    else:
        print("\n\n")
        main()


main()
