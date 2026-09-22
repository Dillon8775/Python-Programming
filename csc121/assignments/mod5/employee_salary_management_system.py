"""
employee_salary_management_system.py:

### Requirements Checklist for Students

Before submitting, make sure your program includes:

* [ ] 8 required functions plus `main()`
* [ ] `pickle` for binary file processing
* [ ] `filter()` with a **lambda** function
* [ ] `map()` with a **lambda** function for the 3% raise
* [ ] `min()` with a **lambda** function
* [ ] `map()` with a **lambda** function for the additional 1% raise
* [ ] `sorted()` with a **lambda** function
* [ ] Salaries displayed as currency
* [ ] Employee information saved to `employees.dat`
* [ ] Employee information loaded from `employees.dat`
* [ ] Meaningful variable and function names
* [ ] Appropriate comments
* [ ] No global employee list
* [ ] Program runs without errors

"""

import pickle

from matplotlib import pyplot as plt


# ---------------------------------------------------------
# Function 1: Get employee information from the user
# ---------------------------------------------------------
def get_employees():
    # TODO:
    # 1. Ask the user how many employees they want to enter.
    # 2. Create an empty list to store employee information.
    # 3. Use a loop to get each employee's name and salary.
    # 4. Store each employee as a tuple:
    #       (name, salary)
    # 5. Add each tuple to the list.
    # 6. Return the list of employees.

    employee_data = []
    number_of_employees = int(input("Enter number of employees: "))
    for i in range(number_of_employees):
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        employee_data.append((name, salary))
    return employee_data

# ---------------------------------------------------------
# Function 2: Save employees to a binary file
# ---------------------------------------------------------
def save_employees(employees):
    # TODO:
    # 1. Open a file named "employees.dat".
    # 2. Open the file in binary write mode.
    # 3. Use pickle.dump() to save the employees list.
    # 4. Display a message confirming that the file was saved.

    with open("employees.dat", "wb") as file:
        pickle.dump(employees, file)
    print("Employee data saved to 'employees.dat'")

# ---------------------------------------------------------
# Function 3: Load employees from the binary file
# ---------------------------------------------------------
def load_employees():
    # TODO:
    # 1. Open "employees.dat" in binary read mode.
    # 2. Use pickle.load() to retrieve the employee list.
    # 3. Return the employee list.

    with open("employees.dat", "rb") as file:
        employee_list = pickle.load(file)

    print("Loaded employee data from 'employees.dat'")
    return employee_list

# ---------------------------------------------------------
# Function 4: Display all employees
# ---------------------------------------------------------
def display_employees(employees):
    # TODO:
    # 1. Display a heading.
    # 2. Use a loop to display each employee's name and salary.
    # 3. Format the salary as currency.
    #
    # Example:
    # John            $42,000.00

    print("\nEmployee\t\tSalary")
    for employee in employees:
        print(f"{employee[0]:<15} ${employee[1]:,.2f}")


# ---------------------------------------------------------
# Function 5: Find employees earning $50,000 or more
# ---------------------------------------------------------
def find_high_paid(employees):
    # TODO:
    # Use filter() with a lambda function to find
    # employees whose salary is $50,000 or more.
    #
    # Remember:
    # Each employee is stored as:
    # (name, salary)
    #
    # Display the employees who meet the requirement.
    #
    # Return the list of high-paid employees.

    high_paid = filter(lambda employee: employee[1] >= 50000, employees)
    print(f"\nHigh Paid directly from filter function: {high_paid}")

    # Wrap the high_paid in list
    high_paid = list(high_paid)
    print(f"\nList wrapped in high paid employees: {high_paid}")

    print("Employees Earning $50,000 or more: ")
    display_employees(high_paid)

    return high_paid

# ---------------------------------------------------------
# Function 6: Give every employee a 3% raise
# ---------------------------------------------------------
def give_raise(employees):
    # TODO:
    # Use map() with a lambda function to give
    # EVERY employee a 3% salary increase.
    #
    # The employee's name should remain unchanged.
    #
    # Return a new list containing the updated employees.

    updated_employees = map(lambda employee: (employee[0], employee[1] * 1.03), employees)
    return list(updated_employees)

# ---------------------------------------------------------
# Function 7: Give the lowest-paid employee an
# additional 1% raise
# ---------------------------------------------------------
def give_lowest_paid_raise(employees):
    # TODO:
    # 1. Use min() with a lambda function to find
    #    the employee with the lowest salary.
    #
    # 2. Give ONLY the lowest-paid employee an
    #    additional 1% raise.
    #
    # 3. You may use map() with a lambda function
    #    to create the updated list.
    #
    # 4. Return the updated employee list.

    lowest_paid_employee = min(employees, key=lambda employee: employee[1])
    updated_employees = map(lambda employee: (employee[0], employee[1] * 1.01) if employee == lowest_paid_employee else employee, employees)
    return list(updated_employees)

# ---------------------------------------------------------
# Function 8: Sort employees by salary
# ---------------------------------------------------------
def sort_by_salary(employees):
    # TODO:
    # Use sorted() with a lambda function to sort
    # employees from HIGHEST salary to LOWEST salary.
    #
    # Display the sorted employees.
    #
    # Return the sorted list.

    sorted_employees = sorted(employees, key=lambda employee: employee[1], reverse=True)
    display_employees(sorted_employees)
    return sorted_employees

# ---------------------------------------------------------
# Function 9: Visualize salary
# ---------------------------------------------------------
def visualize_salary(employees):
    # TODO:
    # Create a bar chart to show employee salaries

    # Get employee
    names = list(map(lambda employee: employee[0], employees))

    # Get employee salaries
    salaries = list(map(lambda employee: employee[1], employees))

    plt.bar(names, salaries, color=['blue', 'green'])
    plt.title("Employee Salaries")
    plt.xlabel("Employee")
    plt.ylabel("Annual Salary")

    plt.show()

    # Create bar chart

# ---------------------------------------------------------
# Main function
# ---------------------------------------------------------
def main():

    print("Employee Salary Management System")
    print("=" * 40)

    # TODO 1:
    # Call get_employees() to get employee information.
    # Store the returned list in a variable.
    # employees = get_employees()

    # TODO 2:
    # Call save_employees() to save the employees
    # to the binary file.
    # save_employees(employees)

    # TODO 3:
    # Call load_employees() to read the employees
    # from the binary file.
    #
    # Replace the employee list with the data
    # loaded from the file.
    employees = load_employees()

    # TODO 4:
    # Call display_employees() to display all employees.
    display_employees(employees)

    # TODO 5:
    # Call find_high_paid() to display employees
    # earning $50,000 or more.
    high_paid = find_high_paid(employees)

    # TODO 6:
    # Call give_raise() to give every employee
    # a 3% raise.
    #
    # Store the updated list.
    updated_employees = give_raise(employees)
    print("After 3% raise:")

    # TODO 7:
    # Call display_employees() to display the
    # employees after the 3% raise.
    display_employees(updated_employees)

    # TODO 8:
    # Call give_lowest_paid_raise() to give the
    # lowest-paid employee an additional 1% raise.
    #
    # Store the updated list.
    additional_updated_employees = give_lowest_paid_raise(updated_employees)

    # TODO 9:
    # Call display_employees() to display the
    # employees after the additional 1% raise.
    print("Lowest paid employee got an additional 1% raise")
    display_employees(additional_updated_employees)

    # TODO 10:
    # Call sort_by_salary() to display employees
    # from highest salary to lowest salary.
    sorted_employees = sort_by_salary(additional_updated_employees)
    display_employees(sorted_employees)

    # TODO 11:
    ## Call visualize_salary() to display the bar chart
    visualize_salary(employees)

# ---------------------------------------------------------
# Start the program
# ---------------------------------------------------------
if __name__ == "__main__":
    main()