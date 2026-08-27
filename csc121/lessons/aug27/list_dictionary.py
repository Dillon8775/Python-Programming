"""
list_dictionary.py: list, tuple, and dictionary
By: D. Strickland
8/27/2026
"""

from common import lineBreak

# list comprehension
def get_even_numbers(numbers:list):
    if type(numbers) is not list:
        return None

    # Traditional way
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

    # Advanced way
    # even_numbers = [num for num in numbers if type(num) is int and if num % 2 == 0]
    return even_numbers

numbers = list(range(10))
print(numbers)
# numbers.append("Numbers") <-- results in TypeError
print(get_even_numbers(numbers))

lineBreak()

# tuple: ummutable ordered sequence
roster = ("Amy", "Bob", "Cindy", "Dave", "Emma")
faculty = ("Michael")

some_students = roster[2:] # Everything after index 2 (starts at index 3)
print(some_students)

some_students = roster[:3] # Stops at index 4 (prints first 3 students)
print(some_students)

some_students = roster[::2] # Jumps 2 for each index (first, 3rd, and 5th in this case)
print(some_students)

print(type(roster))
print(f"type of {type(faculty)}")