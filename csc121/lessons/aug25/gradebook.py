"""
gradebook.py: create a list to store student grades and analyze it
By: D. Strickland
8/25/2026
"""

import matplotlib.pyplot as plt

# Create 2 lists to store students names and scores
names = ["Amy", "Bob", "Charlie", "David"]
scores = [90, 80, 70, 60]
# print(names)
# print(scores)

# Add another name and score
names.append("Emma")
scores.append(100)
# print(names)
# print(scores)

# Len function and use index to visit each element
print(f"There are {len(names)} students in this class.")
for name in names:
    # print(name, end=', ')
    pass

# print()
for index in range(len(scores)):
    # print(f"{names[index]}: {scores[index]:.2f}")
    pass

# Change element value
scores[3] = 88
# print(names)
# print(scores)

print("===")

zipped = zip(names, scores)
print(list(zipped))
for name, score in zipped:
    print(f"{name}: {score:.2f}")

print("===")

number_of_students = len(names)
print(f"Last student in the list: {names[-1]}")

print(f"The first student in the list: {names[0]}")
print(f"Also the first student in the list: {names[-number_of_students]}")

# Slicing
print(f"Starts from the second: {names[1:number_of_students:2]}")

print("===")

# List can be passed and/or returned to/from a function
# Pass the scores and create a pie chart to show the grade distribution
def visualizeScoreDistribution(scores:list):
    """
    :param scores: the list of scores (an int[])
    :return: None
    """
    # Count students in each score range
    score_ranges = ["90-100", "80-89", "70-79", "60-69", "Below 60"]
    counts = [0, 0, 0, 0, 0]
    for score in scores:
        if score >= 90:
            counts[0] += 1
        elif score >= 80:
            counts[1] += 1
        elif score >= 70:
            counts[2] += 1
        elif score >= 60:
            counts[3] += 1
        else:
            counts[4] += 1
        print(counts)

        # Create a pie chart
        colors = ["red", "blue", "green", "yellow", "cyan"]
        plt.pie(counts, labels=score_ranges, colors=colors,
                autopct= '%1.1f%%')
        plt.title("Distribution of student scores")

        # Add legend with counts
        legend_labels = [f"{score_ranges[i]}: {counts[i]} students "
                         for i in range(len(score_ranges))]
        plt.legend(legend_labels, title="Score Range")

        plt.show()

visualizeScoreDistribution(scores)

# Visualize the student scores
def visualizeStudentScore(names, scores):
    colors = ["red", "blue", "green", "yellow", "cyan"]
    plt.bar(names, scores, color=colors)
    plt.title("Student Scores")
    plt.xlabel("Student Names")
    plt.ylabel("Scores")
    plt.show()

visualizeStudentScore(names, scores)