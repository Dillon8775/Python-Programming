"""
dict_set_demo.py: create and use dict and set
By: D. Strickland
9/1/26
"""
import pickle

# create an empty dict
grade_book = {}
grade_book["Amy"] = 100
grade_book["Bob"] = 95
print(grade_book)

# change Amy's grade
grade_book["Amy"] = 99
print(grade_book)

# add Cindy to grades
grade_book["Cindy"] = 98

# ---
# Print type of grade_book
print(f"Type of grade_book:  {type(grade_book)}")

'''
print(grade_book["Amy"])
if "bob" in grade_book:
    print(grade_book["bob"])
else:
    print("bob is not in grade_book")
'''

# ---
# Print all keys (or in this case, names) in grade_book
print("--> Printing all names...")
for name in grade_book.keys():
    print(name)

# ---
# Print all values (or in this case, scores) in grade_book
print("--> Printing all scores...")
for score in grade_book.values():
    print(score)

# ---
# Print all keys and values
print("--> Printing all keys and values...")
print(list(grade_book.keys()))
print(type(grade_book.values()))

# ---
# Pop items from dictionary
print("--> Popping...")
print(grade_book.popitem())
print(grade_book)

# ---
# Create sets
csc118 = ("Amy", "Bob", "Cindy")
csc121 = ("Amy", "Dave", "Emma")

# ---
# Save the grade_book to binary file
print("--> Saving...")
file_object = open("sample_gradebook.data", "wb")
pickle.dump(grade_book, file_object)
file_object.close()

# ---
# Retrieve picked data
print("--> Retrieving data...")
file_object = open("sample_gradebook.data", "rb")
retrieved_data = pickle.load(file_object)
file_object.close()

# Print retrieved data
print(retrieved_data)