"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Department constant defined in ALL_CAPS.
[X] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

DEPARTMENT = "Security operation center"
# security operation center is also known as soc (said as sock)


USERNAME_DEPARTMENT = (
    ("Kubek", "ADMIN"),
    ("Frytek", "EMPLOYEE"),
    ("Zegarek", "EMPLOYEE"),
    ("Bober", "INTERN"),
    ("Bałwanek", "INTERN"),
)
# USERNAME_DEPARTMENT is the nested tuple containing username and employee level

password = ["I<3WATER", "Salty2211", "0utOft!me", "riverd@m22", "WinterCold123"]
# Stored Passwords for all users (very secure)

while True:
    # Runs until user selects option (5) QUIT
    print(f"Welcome to the {DEPARTMENT} security terminal")
    print("\nPlease choose an option below\n")
    print("(1) List usernames")
    print("(2) List passwords for each user")
    print("(3) Change username (admin only)")
    print("(4) Change password (only for employees and admins)")
    print("(5) QUIT")
    break
