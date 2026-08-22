"""
investment_calculator_ds.py: modular program to calculate investment
By: D. Strickland
8/20/2026
"""

# Gets the users investment information
def get_investment_info():
    """
    ask user to input investment amount, apr, and year
    :return: investment amount, apr, and year
    """
    invested_amount = float(input("Enter investment amount: "))
    apr = float(input("Enter APR in number of percentage, enter 3 for 3%: "))
    years = int(input("Enter number of whole years: "))
    return (invested_amount, apr / 100, years)

# Calculates the users investment
def calc_investment(principle, apr, term:int):
    """
    :param principle: the user's invested amount
    :param apr:
    :param term: the term in years (int)
    :return:
    """
    future_value = principle * (1 + apr / 12) ** (term * 12)
    total_interest_earned = future_value - principle
    return future_value, total_interest_earned

# Displays the final invested amount
def display(principle, apr, term:int, future_value, gain):
    """
    :param principle:
    :param apr:
    :param term:
    :param future_value:
    :param gain:
    :return: None
    """
    print(f"\nInvested Amount: ${principle:,.2f}")
    print(f"APR: ${apr:.2%}")
    print(f"Term: {term} years")
    print(f"Future Value: ${future_value:,.2f}")
    print(f"Total Gain: ${gain:,.2f}")

apr = 0.035
print(f"APR: {apr:.2%}")

# Create the main method
def main():
    invested_amount, apr, years = get_investment_info()
    future_value, invested_gain = calc_investment(invested_amount, apr, years)
    display(invested_amount, apr, years, future_value, invested_gain)

# Run main method only in this Python file
if __name__ == "__main__":
    main()