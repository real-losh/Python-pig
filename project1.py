#project 1 - pig

#Allow the user to roll the dice

import random  # Import the random module to access random number generation functions

def roll():  # Define a function named roll
    min_value = 1  # Set the minimum value for the random number to 1
    max_value = 6  # Set the maximum value for the random number to 6

    roll = random.randint(min_value, max_value)  # Generate a random integer between 1 and 6 (inclusive)
                                               # and store it in the variable 'rol'
    return roll  # Return the generated random integer

'''
# Call the roll function and print the result
value = roll()
print(value)'''

# Start an infinite loop to get valid input from the user
while True:
    # Prompt the user to enter the number of players
    players = input("Enter the number of players (2 - 4): ")
    
    # Check if the input is a digit
    if players.isdigit():
        # Convert the input to an integer
        players = int(players)
        
        # Check if the number of players is within the valid range (2 to 4)
        if 2 <= players <= 4:
            # If the input is valid, exit the loop
            break
        else:
            # If the number of players is not within the valid range, print an error message
            print("Must be between 2 - 4 players.")
    else:
        # If the input is not a digit, print an error message
        print("Invalid, try again.")

# Set the maximum score for the game
max_score = 50

# Initialize a list to store the scores for each player, starting with a score of 0
player_scores = [0 for _ in range(players)]

'''
# Print the initialized player scores list
print(player_scores)'''

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn had just started!")
        print("your total score is:", player_scores[player_idx], "/n")
        current_score = 0

        while True:    
            should_roll = input("whould you like to roll (y)?")
            if should_roll.lower() != 'y':
                break

            value = roll() 
            if value == 1:
                print("You rolled a 1! Turn done!")
                #current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score

        print("Your total score is:", player_scores[player_idx] )

# After the while loop, print the final scores
print("\nFinal Scores:")

for idx, score in enumerate(player_scores):
    print(f"Player {idx + 1}: {score}")

# Determine the winner
winner_idx = player_scores.index(max(player_scores))
print(f"\nPlayer {winner_idx + 1} wins! at {player_scores}")