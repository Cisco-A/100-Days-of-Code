# A number guessing game

# get inputs
# You guess a number, and it tells you if it's too high or too low until you get the right number
import random


def game_play(lives):
    end_of_game = False
    while not end_of_game:
        guess = int(input("Make a guess: "))
        if guess != random_number:
            lives = lives - 1
            if lives != 0:
                print(f"You have {lives} attempts remaining.")
                if guess > random_number:
                    print(f"{guess} is too high")
                elif guess < random_number:
                    print(f"{guess} is too low")
                else:
                    end_of_game = True
                    print("You win")
            else:
                end_of_game = True
                print("You lose")
        else:
            end_of_game = True
            print("You win!")


# Initialization

play_again = True
while play_again:
    print("Welcome to the number guessing game")
    print("I'm thinking of a number between 1 - 100")
    difficulty = input("Select a difficulty, 'easy' or 'hard': ").lower()

    lives = 0
    random_number = random.randrange(1, 100)

    if difficulty != "easy" and difficulty != "hard":
        print("You have made an invalid input")

    elif difficulty == "easy":
        lives += 10
        print(random_number)
        print("You have 10 guesses.")
        game_play(lives)


    elif difficulty == "hard":
        lives += 5
        print(random_number)
        print("You have 5 guesses")
        game_play(lives)

    newGame = input("Do you want to play again? Type 'Y' for yes and 'N' for no\n").upper()

    if newGame == "N":
        print("Thanks for playing")
        play_again = False

    elif newGame != "Y" and newGame != "N":
        print("You have made an invalid entry.\nGoodbye!")
        play_again = False
