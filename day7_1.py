import random
#Beginning Steps to building our Hangman game

#Step1

word_list = ["ardvark", "baboon", "camel"]

#Task1 - Randomly selecting a word from the list
chosen_word = random.choice(word_list)

#Task2 - Get the user guessed letter
guess = input("Guess a letter: ").lower()

#Task3 - Check if the letter guessed is in the chosen_word
for i in range(0, len(chosen_word)):
    if guess == chosen_word[i]:
        print(guess)
    else:
        print("Wrong") #As ususal my initial solution is bogus but it helps later as you'll see :)

#Another method for Task3(less complex)
# for letter in chosen_word:
#     if letter == guess:
#         print(guess)
#     else:
#         print("Wrong")