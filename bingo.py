"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""

# --- TASK 1: TUNING THE GUITAR 🎸 ---
instrument = "Acoustic Guitar"
print(f"{instrument} has {len(instrument)} characters in it")
print(f"the first letter of {instrument} is ({instrument[0]})")
print(f"the last letter of {instrument} is ({instrument[-1]})")
print(
    f"the lowest ASCII in {instrument} is ({min(instrument)}) if blank that means it is a space :)"
)
print(
    f"the highest ASCII in {instrument} is ({max(instrument)}) if blank that means it is a space :)"
)

# characters
# --- TASK 2: THE CLEANUP CREW 🎸 ---
messy_input = " vOLUME_knob_11 "
print(messy_input)
print(f"({messy_input}) without spaces is ({messy_input.strip( )})")
messy_input = messy_input.strip()
print(f"({messy_input}) all capitalized is ({messy_input.upper()})")
messy_input = messy_input.upper
# print(
#     f"({messy_input}) with its '_' replaced with spaces is ({messy_input.replace("_"," ")})"
# )
messy_input = messy_input.replace("_", " ")
print(messy_input)
# TODO: Use .replace() to swap the underscores "_" for spaces " "
"""
# --- TASK 3: THE VALIDATOR 🎸 ---
serial_number = "90210"
# TODO: Use .isdigit() to check validity.
# Print "Valid Serial" if it is numeric, or "Invalid Serial" if it isn't.
# --- TASK 4: THE DUCK BRIDGE 🎸🎸 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0
print("\n--- Singing the Duck Song! ---")
# TODO: Create a loop that iterates through name_string (for char in name_string)
# TODO: Inside the loop:
# 1. Use " ".join(duck_letters) to create a variable named 'current_name'
# 2. Print: "There was a teacher who had a duck and Ducky was his Name-o"
# 3. Print the line f"({current_name}) \n" multiplied by 3
# 4. Print "and Ducky was his Name-o!\n"
# 5. Replace the letter in duck_letters at index [count] with "🎸"
# 6. Increment count by 1
# TODO: After the loop, print the "Finale" (the final version with all 🎸 emojis)
# Hint: You'll need one more .join() and one more print block here!
"""
