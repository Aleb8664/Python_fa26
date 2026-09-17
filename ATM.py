"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

print("\033[95mWelcome to ATM\033[0m")
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

while True:
    print("1 ")
    print("2 ")
    print("3 ")
    print("4 ")
    print("5 Exit")
    try:
        user_input = int(input("\nPlease enter choice \033[96mNUMBER\033[0m:  "))
        print(user_input)
    except ValueError:
        print("\n\033[91mPlease Enter NUMERIC value\033[0m")
        continue
