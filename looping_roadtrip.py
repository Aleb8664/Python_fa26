"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[X] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[X] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Funny twist on the are we there yet kids say during road trips. As someone that works for GeekSquad, the tech repair and support center at bestbuy, we get a lot of customers nagging us if their computer is ready for pickup. In this version the program asks for an input after asking if their computer is done yet if the response is "yes" or "y"(done for quickly switching to the 99 bottles portion) after the program gets a response "yes" it prints out what the worker of the computer shop would say "thank you for waiting"
in_service = True
while in_service:
    response = input("Is my computer done yet? (yes/no) :  ").lower()
    if response == "yes" or response == "y":
        in_service = False
print("Thank you for waiting, your computer is now fixed!")
# moving on from the Are we there yet loop, the program automatically goes to the 99 bottles song counting from 99 to 1, the program prints out the full stanza replacing the number of bottles left with the count number counting down. on the last line of the song it is count -1 to represent the bottle being passed around. During the loop there is an if statement checking if the number of bottles is greater than 1 to adjust for the grammatical change in the song when there is only one bottle, once the loop is over it ends and exits into the last print statement using the last count of the loop and eventually ending with 0 at the very end of the song stating there are no more bottles of beer.
for count in range(99, 0, -1):
    if count > 1:
        print(
            f"{count} bottles of beer on the wall, {count} bottles of beer\nTake one down and pass it around, {count-1} bottles of beer on the wall\n"
        )
print(
    f"{count} bottle of beer on the wall, {count} bottle of beer\nTake it down and pass it around, no more bottles of beer on the wall.\n THE END!"
)
