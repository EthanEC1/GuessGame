# This program asks the user guess numbers
# until they guess a correct number. Then the game
# asks them again if they want to play.
import random

# Global list variables
game_history_names = []

game_history_guesses = []

# Main function
def main():
    # Display the scores
    display_scores()

    # Define player
    player = get_player_name()

    # Append player to names
    game_history_names.append(player)

    # Create flag
    is_true = True

    # While flag is true
    while is_true:
        # Repeat/Start game
        is_true = repeat_game()

        # Store name
        store_name(player, game_history_guesses[len(game_history_guesses)-1])

    
# Open history for reading
def read_history():

    # Open history
    file_history = open("history.txt", 'r')

    # Read read lines individually to iterate through them
    current_line = file_history.readline()

    # Read lines with text
    while current_line != "":

        # Remove new line character from player name
        current_player_name = current_line.rstrip("\n")

        # Append player name to game_history_names
        game_history_names.append(current_player_name)

        # Width of 20 characters
        print(f"{current_player_name:<20}", end = "")

        # Remove new line character from player score
        current_player_score = file_history.readline().rstrip("\n")

        # Append player score to history guesses
        game_history_guesses.append(current_player_score)

        # Width of 20 characters
        print(f"{current_player_score:>20}")

        current_line = file_history.readline()

    # Close history.txt    
    file_history.close()

# Function that displays scores
def display_scores():
    # Print name and guesses both at 20 character length
    print(f"{'Name':<20}{'Guesses':>20}")

    # Print 40 lines
    print(f"{'-'*40}")

    # Call read_history()
    read_history()

# Prompt user for name
def get_player_name():

    return input("\n Enter your name: ")

# Function that stores name and guess_value
def store_name(current_name, guess_value):

    # Open file history to append
    file_history = open("history.txt", "a")

    # Write name
    file_history.write(f"\n{current_name}\n")

    # Write guess value
    file_history.write(f"{guess_value}\n")

    # Close
    file_history.close()

# This function starts/repeats the game
def repeat_game():

    # Attempt accumulator
    att = 1

    # Random number between 1 and 100
    random_num = random.randint(1, 100)

    # Set boolean False
    correct = False

    # While not correct = False
    while not correct:
        # Prompt user to guess
        guess = int(input(f"#{att} Guess a number between 1 and 100. "))

        # Incorrect guess, increase attempt number
        while guess != random_num:
            att += 1

            # If guess is lower than radnom num, prompt user again
            if guess < random_num:
                print("Your guess is too low.")
                guess = int(input(f"#{att} Guess a number between 1 and 100. "))

            # If guess is higher than random num, prompt user again
            elif guess > random_num:
                print("Your guess is too high")
                guess = int(input(f"#{att} Guess a number between 1 and 100. "))

        # Set correct to True if answer is correct
        correct = True

        # Congratulate user
        print("Congratulations - you are right!")

        # Append guesses to file   
        game_history_guesses.append(att)

        # Reset attempt number to 1
        att = 1

        # Ask if user would like to play again
        repeat = input("Would you like to play again (y/n)?: ")

    # If answer is yes, return true
    if repeat == "y" or repeat == "Y":

        return True
# Otherwise, return false
    return False

# Call main()
if __name__ == '__main__':
    main()
