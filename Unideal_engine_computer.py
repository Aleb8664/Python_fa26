"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[X] 1. Header Docstring included with assignment title.
[X] 2. Ask user for two integers (num1 and num2).
[X] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[X] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[X] 5. Code is clean and uses descriptive variable names.
[X] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# This is the programs title and instructions for the pit-crew controlling their team's race car engine computer every lap they will read their air temperature readouts and lap number and input this into the program. The program will decide the target boost pressure and power level to best accurately fit the tracks condition to win the race!
print(
    "\nThis is your race car's engine computer\n\nYou will enter a couple of parameters such as:\n   Outside air temperature\n   Lap number 1-10 (1 being the first warmup lap)(~5 will be the middle of the race)(last 2 laps 9 & 10 will be the final push to the finish)\n\n "
)
# this Section will be the inputs for the engine computer calculator so that the computer will calculate the correct power level, this section will ask for the temperature and lap number as an integer value, if a float/decimal value is inputted the program will break due to the user not following directions (not my problem :b )
out_air_temp = int(
    input("please enter a temperature value as a whole integer value:  ")
)
lap_no = int(input("please enter lap number as a whole integer value between 1-10:  "))
# if statement is checking if the user followed directions if directions were not followed the program ends and the user has to re open it and start over
if lap_no < 1 or lap_no > 10:
    print("please follow directions!!!")
    exit()
# the logic to consider which boost pressure and power targets to run, adjusts based on outside temperature and lap number. if temperature is too low the tires are still stiff, every lap the tire gets warmer allowing for more power. the last 2 laps get the highest pressure to get that last little push to win the race. included a logic error at the end in case of a problem.
if out_air_temp < 0 and lap_no < 5:
    print("target boost pressure = 5 psi")
elif out_air_temp < 0 and lap_no == 5:
    print("target boost pressure = 6")
elif out_air_temp < 0 and lap_no > 5 and lap_no < 9:
    print("target boost pressure = 7")
elif out_air_temp < 100 and lap_no < 5:
    print("target boost pressure = 8 ")
elif out_air_temp < 100 and lap_no == 5:
    print("target boost pressure = 9 ")
elif out_air_temp < 100 and lap_no > 5 and lap_no < 9:
    print("target boost pressure = 10")
elif out_air_temp > 100 and lap_no < 9:
    print("target boost pressure = 2")
elif lap_no == 9:
    print("target boost pressure = 15")
elif lap_no == 10:
    print("target boost pressure = 20")
else:
    print("logic error")
