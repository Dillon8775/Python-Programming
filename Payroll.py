# Dillon C. Strickland
# 12/1/2025
# Processes payroll for all hourly paid employees and saves to a text file.

def getEmployeeInfo():
    print("\nEnter employee information:\n")
    employeeID = input("Enter employee id >>>")
    employeeName = input("Enter employee name >>>")
    hoursWorked = float(input("Enter hours worked >>>"))
    hourlyPayRate = float(input("Enter hourly pay rate >>>"))
    return employeeID, employeeName, hoursWorked, hourlyPayRate

def calcGrossPay(hours: float, rate: float):
    if hours > 40:
        overtime = hours - 40
        grossPay = (40 * rate) + (overtime * rate * 1.5)
    else:
        grossPay = hours * rate
    return grossPay

def displayPayStatement(empID: str, empName: str, hoursWorked: float, hourlyPayRate: float, grossPay: float):
    print("\n------------")
    print("Employee ID:", empID)
    print("Employee Name:", empName)
    print("Hours Worked:", hoursWorked)
    print("Hourly Pay Rate:", hourlyPayRate)
    print("Gross Pay:", grossPay)

def savePayStatement(empID: str, empName: str, hoursWorked: float, hourlyPayRate: float, grossPay: float):
    try:
        with open("payroll.txt", "a") as file:
            file.write("-----Payroll-----\n")
            file.write(f"Employee ID: {empID}\n")
            file.write(f"Employee Name: {empName}\n")
            file.write(f"Hours Worked: {hoursWorked:.2f}\n")
            file.write(f"Hourly Pay Rate: ${hourlyPayRate:.2f}\n")
            file.write(f"Gross Pay: ${grossPay:.2f}\n")
            file.write("--------\n\n")
    except:
        print("Error writing to file.")

def main():
    try:
        open("payroll.txt", "w").close()
    except:
        print("Error opening payroll file.")

    totalHours: float = 0
    totalGrossPay: float = 0

    totalEmployees = int(input("Enter total amount of employees >>>"))

    for i in range(totalEmployees):
        employeeID, employeeName, hoursWorked, hourlyPayRate = getEmployeeInfo()
        grossPay = calcGrossPay(hoursWorked, hourlyPayRate)

        displayPayStatement(employeeID, employeeName, hoursWorked, hourlyPayRate, grossPay)

        savePayStatement(employeeID, employeeName, hoursWorked, hourlyPayRate, grossPay)

        totalHours += hoursWorked
        totalGrossPay += grossPay

    print("----")
    print("\nPayroll completed.")
    print(f"Total Employees: {totalEmployees}")
    print(f"Total Hours: {totalHours}")
    print(f"Total Gross Pay: ${totalGrossPay}")
    print("----")

main()