"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[X] 1. Header Docstring included.
[X] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[X] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[X] 4. Task 3: Validation (isdigit check) completed.
[X] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""

print("\n\n")
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
print("\n\n")
# characters
# --- TASK 2: THE CLEANUP CREW 🎸 ---
messy_input = " vOLUME_knob_11 "
print(messy_input)
print(f"({messy_input}) without spaces is ({messy_input.strip( )})")
messy_input = messy_input.strip()
print(f"({messy_input}) all capitalized is ({messy_input.upper()})")
messy_input = messy_input.upper()
print(
    f"({messy_input}) with its '_' replaced with spaces is ({messy_input.replace("_"," ")})"
)
messy_input = messy_input.replace("_", " ")
print(messy_input)
print("\n\n")

# --- TASK 3: THE VALIDATOR 🎸 ---
serial_number = "90210"
print(serial_number)
is_valid = serial_number.isdigit()
if is_valid:
    print(f"{serial_number} is a Valid Serial Number")
else:
    print(f"{serial_number} is not a Valid Serial Number")
print("\n\n")


# --- TASK 4: THE DUCK BRIDGE 🎸🎸 ---
# We are going to sing about a Duck!
# We can't change strings (immutable), so we convert to a list
name_string = "DUCKY"
duck_letters = list(name_string)
count = 0
current_name = ""
ext = 0
print("\n--- Singing the Duck Song! ---")
for char in name_string:
    current_name = " ".join(duck_letters)
    print("There was a teacher who had a duck and Ducky was his Name-o")
    print(f"({current_name}) \n" * 3)
    duck_letters[count] = "🎸"
    count = count + 1
    ext = count

finale = " ".join(duck_letters)
print("There was a teacher who had a duck and Ducky was his Name-o")
current_name = " ".join(duck_letters)
print(f"({current_name}) \n" * 3)
duck_letters[ext - 1] = "🎸"
print("end")
