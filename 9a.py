"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


def get_prices(size):
    match size.lower():
        case "small":
            return 3.00
        case "medium":
            return 4.00
        case "large":
            return 5.00
        case _:
            print("Invalid choice")
            return 0.00


def blend(size, base, fruit, scoops):
    pass


# It should use the order details and price to print a description of the smoothie.


def main():
    print("test")
    selection = input("please select size:  ")
    price = get_prices(selection)
    print(f"price is ${price}")
    # TODO: make an actual menu


main()
