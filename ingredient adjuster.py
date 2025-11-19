# Dillon C. Strickland
# 11/18/2025
# Calculates how much sugar, butter and flour you will need to make a certain amount of cookies.
number_of_cookies = int(input("How many cookies do you want to make?\n>>>"))

sugar = (1.5 / 48) * number_of_cookies
butter = (1 / 48) * number_of_cookies
flour = (2.75 / 48) * number_of_cookies

print(f"To bake {number_of_cookies} cookies you will need:")
print(f"Sugar: {sugar} cups")
print(f"Butter: {butter} cups")
print(f"Flour: {flour} cups")