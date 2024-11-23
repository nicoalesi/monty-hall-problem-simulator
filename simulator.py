from os import _exit
from random import choice, randint

# This file cointains all the necessary code to simulate n times the
# Monty Hall problem and measure the probability of the outcomes.

# MAIN function
def main():
    # Ask the user how many times he wants to simulate the problem.
    # If the input is not a number reject it and end the program.
    try:
        simulations = int(input("Simulations: "))
    except ValueError:
        exit("The value you inserted is not a number.")

    # Variable to keep track of wins obtained without changing choice.
    wins = 0

    # Simulate n times.
    for i in range(simulations):
        # Choose one door randomly, this is the door with the prize.
        prize = randint(1, 3)
        # Create a set to store the remaining two doors with goats.
        goats = {1, 2, 3} - {prize,}
        # Simulate the player's choice.
        choice = randint(1, 3)
        # Open one of the two doors with the goat and let the imaginary
        # player decide what to do (change or keep his choice).
        #   For this experiment there is no need to actually change the
        #   door, we can just keep track of the wins without changing it
        #   and calculate the losses to have the changing door win rate.

        # Since the revelation doesn't change our choice, we can just
        # check if we won or lost.
        if choice == prize:
            wins += 1

    # Calculate the percentages and print the results.
    keep_win_rate = (wins / simulations) * 100
    change_win_rate = 100 - keep_win_rate
    print(f"Win rate keeping our choice:   {keep_win_rate:.2f}%")
    print(f"Win rate changing our choice:  {change_win_rate:.2f}%")


if __name__ == "__main__":
    main()