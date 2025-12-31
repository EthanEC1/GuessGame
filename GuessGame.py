# This program asks the user guess numbers
# until they guess a correct number. Then the game
# asks them again if they want to play.
import random

# Global list variables
game_history_names = []

game_history_guesses = []

# Main function
def main():
    display_scores()

    player = get_player_name()

    game_history_names.append(player)

    is_true = True

    # While true
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

    # Read lines with text while current line is not blank
    while current_line != "":
        current_player_name = current_line.rstrip("\n")
        
        game_history_names.append(current_player_name)

        print(f"{current_player_name:<20}", end = "")

        current_player_score = file_history.readline().rstrip("\n")

        game_history_guesses.append(current_player_score)

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
    file_history = open("history.txt", "a")
    file_history.write(f"\n{current_name}\n")
    file_history.write(f"{guess_value}\n")

    file_history.close()

# This function starts/repeats the game
def repeat_game():
    att = 1
    random_num = random.randint(1, 100)
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
        print("Congratulations - you are right!")

        game_history_guesses.append(att)

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

