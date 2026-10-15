"""this program is an inventory program to help keep track of what products are available for various types of use cases. program can be used for products for sale, buisness consumables (cleaning supplies, office supplies, medical supplies,ETC) and for tools that can be used. Program will track who checks an item out, when it was checked out, and user will have to input a reason for checking out to help locate the item if it is lost. Program will check if user is authorized to check an item out and block unauthorized use of a product. each product can be set with a max check out time that makes a banner at the top of the menu for 'lost' items that need to be renewed or returned. program will notify if any stock is running low for consumable and sale products. Authorized users can add or remove products in cases of new items for sale or worn out tools for replacement or out of commission"""


def user():
    # gets the current users user id
    pass


def lost_timer():
    # loads all checked out items and compares them to the current date and time to display which items are considered lost and need to be accounted for
    pass


def add_product():
    # checks for user authorization and asks user the name of the product, location of storage, quantity, max quantity, max check out length, max renewal. then creates a record for this product in the corresponding location
    pass


def remove_product():
    # checks for user authorization, asks which product to remove, asks if change is permanent or temporary. if change is permanent it deletes the record of the product and creates a record of deletion. if it is a temporary removal it adds the out of stock/out of commision tag to the product
    pass


def checkout():
    # checks for user authorization. user can search for a product based on location or product ID or name, allows user to check out if authorized and displays the due date and asks user if they would like a recipt and creates a record of the checked out item
    pass


def checkin():
    # user has to scan items barcode or input its ID to check the item in, marks the record as checked in and makes the item available for checkout again.
    pass


def main():
    print("start")
    print("end")


main()
