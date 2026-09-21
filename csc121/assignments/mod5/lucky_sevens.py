"""
lucky_sevens.py: A game of lucky sevens, which is flawed, but works.
By: Dillon. S
9/21/26
"""

import random
import sys

# Increase recursion depth limit
sys.setrecursionlimit(20000)

"""
Recursive function that calls itself until pot_amount is 0
"""
def play_game(pot_amount:float, game_counter:int):
    # Stop when pot equals 0
    if pot_amount <= 0:
        return game_counter

    # Print information
    print(f"Game #{game_counter}!")
    print(f"Pot Amount: ${pot_amount:,.2f}")

    # Generate dice numbers
    dic1 = random.randint(1, 6)
    dic2 = random.randint(1, 6)

    # Add up result
    result = dic1 + dic2

    # Player wins $4 if dice add up to 7
    if result == 7:
        pot_amount += 4
    else:
        pot_amount -= 1 # Otherwise, player loses $1

    # Increment game counter and call recursively
    return play_game(pot_amount, game_counter + 1)

# Define main function, where user can input money amount
def main():
    money_amount = int(input("Enter amount of money: "))
    games = play_game(money_amount, 0)

    print(f"\nGames played: {games}")

# Run main function
if __name__ == "__main__":
    main()