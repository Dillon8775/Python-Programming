# Dillon C. Strickland
# 11/24/2025
# Prints the largest number inputted by the user.

count = 0
highest = None
lowest = None
total = 0

number = input("Enter a number, or press enter to stop.\n>>>")

while number != "":
    number = int(number)
    count += 1
    total += number

    if highest is None:
        highest = number
        lowest = number
    else:
        if number > highest:
            highest = number
        elif number < lowest:
            lowest = number

    number = input("Enter next number, or press enter to stop.\n>>>")

if count != 0:
    average = total / count

    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)
else:
    print("No number entered")