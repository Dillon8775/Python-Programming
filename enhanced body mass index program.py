# Dillon C. Strickland
# 11/19/2025
# Calculates the user's body mass index.
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight * 703 / height ** 2

if bmi >= 18.5 and bmi <= 25:
    print("You have an optimal body mass index!")
elif bmi < 18.5:
    print("You are underweight.")
elif bmi > 25:
    print("You are overweight.")