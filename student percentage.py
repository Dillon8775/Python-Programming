# Dillon C. Strickland
# 11/18/2025
# Calculates the percentage of males and females in a class.
males = int(input("Enter amount of males: "))
females = int(input("Enter amount of females: "))

males_percentage = males / (males + females)

print(f"The percentage of males: {males_percentage * 100}%")
print(f"The percentage of females: {100 - (males_percentage * 100)}%")