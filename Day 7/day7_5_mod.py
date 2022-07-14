#Final Part
#The Hangman Game
import random
import hangman_art as ha
import hangman_words as hw

chosen_word = random.choice(hw.word_list)
lives = 6

print(ha.logo)

# Testing code
# print(f'Psst, the solution is {chosen_word}.')  # Let's print this for confirmation for now

display = []
for letter in chosen_word:
    display.append("_")
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess} ")

    # Check guessed letter
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess  # I told you my method would save the day

    if guess not in chosen_word:
        print(f"The letter you selected {guess}, is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # Making all the elements a string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(ha.stages[lives])
