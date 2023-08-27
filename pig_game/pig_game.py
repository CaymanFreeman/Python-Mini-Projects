import random
from time import sleep

print("\nWelcome to Pig, a simple game of chance.")
print('''
Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides not to roll.
- If the player rolls a 1, they score nothing and it becomes the next player's turn.
- If the player rolls any other number, it is added to their turn total and the player's turn continues.
- If a player chooses not to roll, their turn total is added to their score, and it becomes the next player's turn.
The first player to score the agreed upon score (traditionally 100) or above wins.
- If multiple players have reached the agreed upon score, the player with the highest score wins.
''')

while True:
    players = input("Enter the number of players (2 to 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("\nThere must be 2 to 4 players.")
    else:
        print("\nInvalid input, please enter a whole positive number.")

player_scores = [0 for _ in range(players)]

while True:
    winning_score = input("What score would you like to play to?: ")
    if winning_score.isdigit():
        winning_score = int(winning_score)
        if 0 < winning_score <= 500:
            break
        else:
            print("\nYou can only play to a score from 0 to 500.")
    else:
        print("\nInvalid input, please enter a whole positive number.")


def roll_die():
    print("\nRolling die...")
    min_value = 1
    max_value = 6
    num = random.randint(min_value, max_value)
    sleep(0.5)
    print(f"You've rolled a {num}.")
    return num


while max(player_scores) < winning_score:
    for i in range(players):
        print(f"\nCurrent turn: Player {i + 1}\nCurrent score: {player_scores[i]}")
        turn_score = 0

        while True:
            should_roll = input("Would you like to roll the die (y/n)?: ")
            if should_roll.lower() != "y":
                break
            rolled_value = roll_die()
            if rolled_value == 1:
                turn_score = 0
                break
            else:
                turn_score += rolled_value
            print(f"\nYour earned score for this turn is: {turn_score}.")

        player_scores[i] += turn_score
        print(f"\nPlayer {i + 1}'s cumulative score for the game is: {player_scores[i]}.")

max_score = max(player_scores)
winning_player = player_scores.index(max_score)
print(f"\nPlayer {winning_player + 1} is the winner with a score of {max_score}!")
