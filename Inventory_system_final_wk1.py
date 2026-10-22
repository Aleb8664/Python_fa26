"""this program is an inventory program to help keep track of what products are available for various types of use cases. program can be used for products for sale, buisness consumables (cleaning supplies, office supplies, medical supplies,ETC) and for tools that can be used. Program will track who checks an item out, when it was checked out, and user will have to input a reason for checking out to help locate the item if it is lost. Program will check if user is authorized to check an item out and block unauthorized use of a product. each product can be set with a max check out time that makes a banner at the top of the menu for 'lost' items that need to be renewed or returned. program will notify if any stock is running low for consumable and sale products. Authorized users can add or remove products in cases of new items for sale or worn out tools for replacement or out of commission"""

# ❗Citing source, I wanted to use colors to improve readability of the program. I found the text being all one color made it tricky to figure out what was happening. the source I used for this program is "https://www.geeksforgeeks.org/python/print-colors-python-terminal/#google_vignette" I used the first example print statement. the print statement included the \033[NUMBERm which i used as a template for the future. i also noticed if you dont ad \033[0m to the end of the print statement it continues using that color. I also asked copilot to list all the common ansi colors with the number code listed below!

"""
Black: \033[30m
Red: \033[31m
Green: \033[32m
Yellow: \033[33m
Blue: \033[34m
Magenta: \033[35m
Cyan: \033[36m
White: \033[37m
Bright Black: \033[90m
Bright Red: \033[91m
Bright Green: \033[92m
Bright Yellow: \033[93m
Bright Blue: \033[94m
Bright Magenta: \033[95m
Bright Cyan: \033[96m
Bright White: \033[97m
"""

# TODO: make a system to make item ID to simplify the passing variables.
import os


#!!!! citation for clear screen https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python used the example code and put it in a function
def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


def user(id):
    if id == 1:
        clear_screen()
        return "aleb"
    pass


def lost_timer():
    # loads all checked out items and compares them to the current date and time to display which items are considered lost and need to be accounted for
    pass


def add_product():
    # checks for user authorization and asks user the name of the product, location of storage, quantity, max quantity, max check out length, max renewal. then creates a record for this product in the corresponding location
    pass


def remove_product():
    # checks for user authorization, asks which product to remove, asks if change is permanent or temporary. if change is permanent it deletes the record of the product and creates a record of deletion. if it is a temporary removal it adds the out of stock/out of commission tag to the product
    pass


def checkout():
    # checks for user authorization. user can search for a product based on location or product ID or name, allows user to check out if authorized and displays the due date and asks user if they would like a recipt and creates a record of the checked out item
    pass


def checkin():
    # user has to scan items barcode or input its ID to check the item in, marks the record as checked in and makes the item available for checkout again.
    pass


def main():
    clear_screen()
    userID = int(input("1. Please enter your employee ID number:  "))
    username = user(userID)
    print(f"Welcome \033[36m{username}\033[0m please select your options below:")
    print("1.ADD ITEM")
    print("2.REMOVE ITEM")
    print("3.CHECK IN ")
    print("4.CHECK OUT")
    print("5.")
    print("6.\033[91mEXIT\033[0m")


main()
