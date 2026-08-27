"""
weekly_pay_calculator.py: program that calculates a user's weekly pay.
By: D. Strickland
8/23/2026
"""

# Gets number of hours worked and hourly pay rate
def get_hoursworked_and_hourlyrate():
    hours_worked = float(input("Enter number of hours worked: "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    return hours_worked, hourly_pay_rate

# Calculates gross pay
def calc_gross_pay(
        hours_worked:float,
        hourly_pay_rate:float,
        full_time_hours:int = 40,
        over_time_multiplier:float = 1.5
):
    """
    Calculates and return gross pay with specified overtime pay rate
    :param hours_worked: float
    :param hourly_pay_rate: float
    :param full_time_hours: int, 40 by default
    :param over_time_multiplier: float, 1.5 times of hourly_pay_rate by default
    :return: float
    """
    # pay all hours at regular rate:
    gross_pay = hours_worked * hourly_pay_rate
    # check if hours worked greater than the specified full time hours
    if hours_worked > full_time_hours:
        overtime_hours = hours_worked - full_time_hours
        overtime_pay = overtime_hours * hourly_pay_rate * (over_time_multiplier - 1)
        gross_pay += overtime_pay
    return gross_pay

# Prints pay stub in accounting format
def print_pay_stub(hours_worked:float, hourly_pay_rate:float, gross_pay:float):
    """
    :param hours_worked: float
    :param hourly_pay_rate: float
    :param gross_pay: final gross pay (float)
    :return: None
    """
    print(f"\nTotal Number of Hours Worked: {hours_worked}")
    print(f"Hourly Pay Rate: ${hourly_pay_rate:,.2f}")
    print(f"Your Gross Pay: ${gross_pay:,.2f}")

# Create main method
def main():
    hours_worked, hourly_pay_rate = get_hoursworked_and_hourlyrate()
    gross_pay = calc_gross_pay(hours_worked, hourly_pay_rate)
    print_pay_stub(hours_worked, hourly_pay_rate, gross_pay)

# Runs main method only in this Python file
if __name__ == "__main__":
    main()