'''
Ryan Gardanier
IS 303
Dice Game

Inputs: 
- user inputs their name
- user responds with a yes or no if they want to play
- make sure to use the try/except block to catch any errors that may occur

Processes: 
- get_input() function to get the user's name and if they want to play
- roll_dice() function that returns the user's roll and the computer's roll
- compare_rolls(users number, computer's number) function that compares the rolls and determines the winner and returns the results
- main() function that calls the other functions and runs the game
- print(users_number, computers_number, results) function that prints the results of the game

Outputs:
- print the results of the game, including the user's roll, the computer's roll, and who won
'''
import random

def get_name():
    name = input("Enter your name: ")
    return name


def get_input():
    while True:
        try:
            amount_of_rounds = int(input("How many rounds do you want to play? "))
            if amount_of_rounds < 1:
                raise ValueError("Please enter a positive integer greater than 0.")
            print(f"Alright, let's play {amount_of_rounds} rounds!")
            return amount_of_rounds
        except ValueError:
            print("I'm sorry, please enter a positive integer.")

def roll_dice():
    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    return player_roll, computer_roll


def compare_rolls(player_roll, computer_roll, computer_wins, player_wins):
    if player_roll > computer_roll:
        result = "You win!"
        player_wins += 1
    else:
        result = "You lost, the computer won :)"
        computer_wins += 1
    return result, player_wins, computer_wins


def print_result(result, player_roll, computer_roll, player_wins, computer_wins):
    print(f"Your roll: {player_roll}")
    print(f"Computer's roll: {computer_roll}")
    print(result)
    print(f"your total wins: {player_wins}/{player_wins + computer_wins}")
    print(f"computer's total wins: {computer_wins}/{player_wins + computer_wins}")


def main():
    name = get_name()
    amount_of_rounds = get_input()
    rounds = 0
    computer_wins = 0
    player_wins = 0
    while rounds < amount_of_rounds:
        player_roll, computer_roll = roll_dice()
        result, player_wins, computer_wins = compare_rolls(player_roll, computer_roll, computer_wins, player_wins)
        print_result(result, player_roll, computer_roll, player_wins, computer_wins)
        rounds += 1
        input("Press Enter to continue to the next round...")
    print("Thanks for playing!")


if __name__ == '__main__':
    main()