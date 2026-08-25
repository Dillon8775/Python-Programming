"""
gradebook.py: create a list to store student grades and analyze it
By: D. Strickland
8/25/2026
"""

# Create 2 lists to store students names and scores
names = ["Amy", "Bob", "Charlie", "David"]
scores = [90, 80, 70, 60]
print(names)
print(scores)

# Add another name and score
names.append("Emma")
scores.append(100)
print(names)
print(scores)

# Len function and use index to visit each element
print(f"There are {len(names)} students in this class.")
for name in names:
    print(name, end=', ')

print()
for index in range(len(scores)):
    print(f"{names[index]}: {scores[index]:.2f}")

# Change element value
scores[3] = 88
print(names)
print(scores)