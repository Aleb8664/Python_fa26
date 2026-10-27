"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime


def main():
    while True:
        try:
            ask = input("Do you have an error? Y/N:  ").lower()
            if ask == "n" or ask == "no":
                break

        except Exception as e:
            print(f"{ask} is not a valid input. error: {e}")

    with open("bug_tracker.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}\n")
    pass


main()
