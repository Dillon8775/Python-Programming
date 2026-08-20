"""
investment_calculator_ds.py: modular program to calculate investment
By: D. Strickland
8/20/2026
"""

def main():
    invested_amount, apr, years = get_investment_info()
    future_value, invested_gain = calc_investment(invested_amount, apr, years)
    display(future_value, apr, years, future_value, invested_gain)

def get_investment_info():
    """
    ask user to input investment amount, apr, and year
    :return: investment amount, apr, and year
    """
    invested_amount = float(input("Enter investment amount: "))
    apr = float(input("Enter APR in number of percentage, enter 3 for 3%: "))
    years = int(input("Enter number of whole years: "))
    return (invested_amount, apr / 100, years)

def calc_investment(invested_amount, apr, years):
    """
    :param invested_amount:
    :param apr:
    :param years:
    :return:
    """
    pass

def display(invested_amount, apr, years, future_value, investment_gain):
    """
    :param invested_amount:
    :param apr:
    :param years:
    :param future_value:
    :param investment_gain:
    :return: None
    """
    print(f"Invested Amount: ${invested_amount:,.2f}")
    print(f"APR: ${apr:.2%}")

apr = 0.035
print(f"APR: {apr:.2%}")

if __name__ == "__main__":
    main()