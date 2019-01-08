import random

# Text header
print("---------------------------------------------")
print("    Welcome to the Number Guessing Game")
print("---------------------------------------------")
#Game
def start_game():
    random_number = random.randint(1, 10)

# Prompt user for guesses, higher or lower + Exceeds credit (keeps guesses in a number range i.e 1-10)
    try:
        guess = int(input("Guess a number between 1 and 10:   "))
        guess_count = 1
        print("***{} guesses so far***".format(guess_count))
    except ValueError:
        print("### Do not use letters, numbers only ###")
        start_game()

    while guess != random_number:
        try:
            if guess > 10 or guess < 0:
                print("Oh no! ONLY use a number between 1 and 10.")
                guess = int(input("Enter a number between 1 and 10:   "))
                guess_count += 1
                print("***{} guesses so far***".format(guess_count))
            elif guess > random_number:
                print("Nope! Too high, try again.")
                guess = int(input("Enter a number between 1 and 10:   "))
                guess_count += 1
                print("***{} guesses so far***".format(guess_count))
            elif guess < random_number:
                print("Nope! Too low, try again.")
                guess = int(input("Enter a number between 1 and 10:   "))
                guess_count += 1
                print("***{} guesses so far***".format(guess_count))
        except ValueError:
            print("### Do not use letters, numbers only ###")

# Exceeds Credit - Highscore
    high_score = 0 
    if guess_count >= high_score:
        high_score = guess_count
    else:
        guess_count < high_score
        high_score = high_score

# Winning Code + exceeds credit "Prompt for a replay"
    print("Congratulations! You guessed the random number! Great job!")
    print("***It took you {} guesses to win!***".format(guess_count))
    play_again = input("Want to play again? [yes] [no]\n")


# Exceeds Credit - Replay Code

# Winning Code + exceeds credit "Prompt for a replay"
    if play_again.lower() == 'yes':
        print("    -----The Current Highscore is {}-----".format(high_score))
        start_game()
    elif play_again.lower() == 'no':
        print("Thank you for playing!")
    else:
        print("Thank you for playing!")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
