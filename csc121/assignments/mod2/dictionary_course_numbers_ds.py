"""
dictionary_course_numbers.py: stores course numbers and room numbers with dictionaries
By: D. Strickland
9/1/26
"""

__author__ = "Dillon Strickland"

# Create valid course number variables
cs101 = "CS101"
cs102 = "CS102"
cs103 = "CS103"
nt110 = "NT110"
cm241 = "CM241"

# Create room number dictionary
roomNumbers = {
    cs101 : 3004,
    cs102 : 4501,
    cs103 : 6755,
    nt110 : 1244,
    cm241 : 1411
}

# Create instructor dictionary
instructors = {
    cs101 : "Haynes",
    cs102 : "Alvarado",
    cs103 : "Rich",
    nt110 : "Burke",
    cm241 : "Lee"
}

# Create meeting time dictionary
meetingTimes = {
    cs101 : "8:00 a.m.",
    cs102 : "9:00 a.m.",
    cs103 : "10:00 a.m.",
    nt110 : "11:00 a.m.",
    cm241 : "1:00 p.m."
}

# Prompt user to enter valid course number
userInput:str = input(f"Enter course number:\n{cs101}\n{cs102}\n{cs103}\n{nt110}\n{cm241}\n--> ")
# Make input upper case
userInput = userInput.upper()

# Track if room number was found and entered correctly
found:bool = False

for s in roomNumbers:
    # If it was found, print out required information and stop program
    if userInput == s:
        print(f"Room Number: {roomNumbers.get(userInput)}")
        print(f"Instructor: {instructors.get(userInput)}")
        print(f"Meeting Time: {meetingTimes.get(userInput)}")
        found = True
        break

# If user entered an invalid course number, warn user and stop program
if not found:
    print("Invalid room number! Please try again.")