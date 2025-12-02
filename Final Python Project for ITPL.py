# Dillon C. Strickland
# 11/23/2025
# Final project for class, designed to store and output grades.

def getClassInfo():
    print("\n----\n")
    className = input("Enter class name\n>>>")
    facultyName = input("Enter faculty name\n>>>")
    numberOfStudents = int(input("Enter number of students\n>>>"))
    studentInfo = []
    for i in range(numberOfStudents):
        studentName = input(f"Enter student #{i+1} name\n>>>")
        studentScore = float(input("Enter student % score\n>>>"))
        studentInfo.append([studentName, studentScore])
    return className, facultyName, studentInfo

def calcGrade(score: float):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    className, facultyName, studentInfo = getClassInfo()

    print(className)
    print(facultyName)
    print("\n")
    print("Student Name     Number Score     Letter Grade")
    numberOfAs: int = 0
    numberOfBs: int = 0
    numberOfCs: int = 0
    numberOfDs: int = 0
    numberOfFs: int = 0
    letterGrades = []
    for student in studentInfo:
        letterGrade = calcGrade(student[1])
        if letterGrade == "A":
            numberOfAs += 1
        elif letterGrade == "B":
            numberOfBs += 1
        elif letterGrade == "C":
            numberOfCs += 1
        elif letterGrade == "D":
            numberOfDs += 1
        else:
            numberOfFs += 1
        letterGrades.append(letterGrade)
        print(student[0], "             ", student[1], "            ", letterGrade)
    print("-----")
    print("Number of As: ", numberOfAs)
    print("Number of Bs: ", numberOfBs)
    print("Number of Cs: ", numberOfCs)
    print("Number of Ds: ", numberOfDs)
    print("Number of Fs: ", numberOfFs)

    with open(className + facultyName + "Grades.txt", "w") as file:
        file.write("-----"+className+", " + facultyName+"------")
        file.write("\n\nStudent Information:\n")
        count: int = 0
        for student in studentInfo:
            file.write(student[0] + ", " + str(student[1]) + " / " + letterGrades[count] + "\n")
            count += 1
        file.write("\n")
        file.write("Number of As: " + str(numberOfAs)+"\n")
        file.write("Number of Bs: " + str(numberOfBs)+"\n")
        file.write("Number of Cs: " + str(numberOfCs)+"\n")
        file.write("Number of Ds: " + str(numberOfDs)+"\n")
        file.write("Number of Fs: " + str(numberOfFs)+"\n")
        file.write("-----")
        file.close()

main()