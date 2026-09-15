"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

print("welcome to the Dance Dance Revolution (DDR) ticket booth\n")
more_tickets = True
while more_tickets:
    while True:
        try:
            num_dancers = int(input("How many dancers? 1-4:  "))
            if num_dancers >= 1 and num_dancers <= 4:
                break
            print(
                f"{num_dancers} is not a valid number of dancers please enter 1-4 dancers"
            )
        except ValueError:
            print("value error")
    while True:
        ask = input("would you like more tickets Y/N:  ").lower()
        if ask != "y" and ask != "n":
            print("* please enter Y for yes or N for no *")
        elif ask == "n":
            more_tickets = False
            break
