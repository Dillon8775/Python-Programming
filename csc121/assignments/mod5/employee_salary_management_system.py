"""
employee_salary_management_system.py: Prints and stores employee information in bar and text form.
By: Dillon. S
9/23/26
"""

import pickle

from matplotlib import pyplot as plt


def get_employees():
    """
    Asks the user how many employees they want to store,
    then creates an empty list to store the information,
    and uses a loop to get each employee's name and salary.
    :return: the list of employees.
    """
    employee_data = []
    number_of_employees = int(input("Enter number of employees: "))
    for i in range(number_of_employees):
        name = input("Enter employee name: ")
        salary = float(input("Enter employee salary: "))
        employee_data.append((name, salary))
    return employee_data

def save_employees(employees):
    """
    Opens the 'employees.dat' file in binary write mode,
    utilizing pickle.dump() to save employees list.
    :param employees: the employees to save
    :return: None
    """
    with open("employees.dat", "wb") as file:
        pickle.dump(employees, file)
    print("Employee data saved to 'employees.dat'")

def load_employees():
    """
    Opens the 'employees.dat' file in binary read mode,
    and loads the employee list
    :return: the employee list
    """
    with open("employees.dat", "rb") as file:
        employee_list = pickle.load(file)

    print("Loaded employee data from 'employees.dat'")
    return employee_list

def display_employees(employees):
    """
    Displays all employees name and salary from the employee list
    :param employees: the employees to display
    :return: None
    """
    print("\nEmployee\t\tSalary")
    for employee in employees:
        print(f"{employee[0]:<15} ${employee[1]:,.2f}")

def find_high_paid(employees):
    """
    Utilizes the filter() functon with a lambda to find employees with a salary of $50,000 or more.
    :param employees: the employees to check
    :return: the highest paid employee
    """
    high_paid = filter(lambda employee: employee[1] >= 50000, employees)
    print(f"\nHigh Paid directly from filter function: {high_paid}")

    # Wrap the high_paid in list
    high_paid = list(high_paid)
    print(f"\nList wrapped in high paid employees: {high_paid}")

    print("Employees Earning $50,000 or more: ")
    display_employees(high_paid)

    return high_paid

def give_raise(employees):
    """
    Gives each employee a 3% raise by utilizing a map() lambda function.
    :param employees: the list of employees to give the raise to
    :return: the new list of employees with their raise
    """
    updated_employees = map(lambda employee: (employee[0], employee[1] * 1.03), employees)
    return list(updated_employees)

def give_lowest_paid_raise(employees):
    """
    Gives the lowest paid employee a 1% raise by utilizing map() function
    :param employees: the list of employees to check for lowest paid employee
    :return: the new list of employees, with the lowest paid employee a 1% raise
    """
    lowest_paid_employee = min(employees, key=lambda employee: employee[1])
    updated_employees = map(lambda employee: (employee[0], employee[1] * 1.01) if employee == lowest_paid_employee else employee, employees)
    return list(updated_employees)

def sort_by_salary(employees):
    """
    Sorts the employee list using the sorted() lambda function, from highest to lowest salary.
    :param employees: the employees list to sort
    :return: the sorted employee list
    """
    sorted_employees = sorted(employees, key=lambda employee: employee[1], reverse=True)
    display_employees(sorted_employees)
    return sorted_employees

def visualize_salary(employees):
    """
    Visualizes the employees salary by creating a bar chart.
    :param employees: the employees to visualize
    :return: None
    """

    # Get employee
    names = list(map(lambda employee: employee[0], employees))

    # Get employee salaries
    salaries = list(map(lambda employee: employee[1], employees))

    plt.bar(names, salaries, color=['blue', 'green'])
    plt.title("Employee Salaries")
    plt.xlabel("Employee")
    plt.ylabel("Annual Salary")

    # Create bar chart
    plt.show()

def main():
    print("Employee Salary Management System")
    print("=" * 40)

    # Load employees
    employees = load_employees()

    # Display employee data
    display_employees(employees)

    # Find highest paid employee
    high_paid = find_high_paid(employees)

    # Give 3% raise to each employee
    updated_employees = give_raise(employees)
    print("After 3% raise:")

    # Print updated employees
    display_employees(updated_employees)

    # Give employee with lowest salary a 1% raise
    additional_updated_employees = give_lowest_paid_raise(updated_employees)

    # Display updated employees
    print("Lowest paid employee got an additional 1% raise")
    display_employees(additional_updated_employees)

    # Sorts employees by their salary
    sorted_employees = sort_by_salary(additional_updated_employees)
    display_employees(sorted_employees)

    # Visualizes employee salaries
    visualize_salary(employees)

# Run the main method
if __name__ == "__main__":
    main()