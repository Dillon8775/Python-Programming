"""
review_basics.py: review basics of Python
by D. Strickland
08/18/2026
"""

import keyword as theKeywordList

__author__ = "Dillon Strickland" # Author
__email__ = "stricklandd0778@forsythtech.edu" #E-mail

# Print number of keywords in Python
print(f"There are {len(theKeywordList.kwlist)} keywords defined in this version of Python.")

# Returns: if a string is a valid identifier/str
def isValidIdentifier(identifier_name:str):
    # test if a given word is a keyword
    if theKeywordList.iskeyword(identifier_name):
        # print(f"[ERROR] {identifier_name} is a keyword.")
        return True
    else:
        # print(f"[SUCCESS] {identifier_name} is not a keyword.")
        return False

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

# the calc_gross_pay with 50 hours worked and $10 per hour, with default 40 and 1.5
print(f"Gross Pay: ${calc_gross_pay(40, 10)}")

# the cal_gross_pay with 50 hours worked and $10 per hour, with default 40 and 1.5
print(f"Gross Pay: ${calc_gross_pay(50, 10)}")

# the calc_gross_pay with 40 hours worked and $10 per hour, full time hours is 30 (40 is replaced with 30, since it is optional)
print(f"Gross Pay: ${calc_gross_pay(30, 10, 30, over_time_multiplier=2)}")

# Print documentation comment
print(__doc__)

print("Hello, and goodbye!", end=" woah")