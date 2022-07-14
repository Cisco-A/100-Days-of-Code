# Step3
# Initialization
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Psst, the solution is {chosen_word}.')  # Let's print this for confirmation for now

display = []
for letter in chosen_word:
    display.append("_")
print(display)

# Use a while loop to let the user guess again until all the letters of the word have been guessed
# Print they have won

end_of_game = False
while not end_of_game:  # Was stuck on this while loop condition for 2 days💔
    guess = input("Guess a letter: ").lower()

    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess  # I told you my method would save the day
    print(display)

    if "_" not in display:
        end_of_game = True
print("You win")
