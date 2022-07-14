#Step4
#I decided to make this mod so we use our own code format... The cool one😉
import random
#Initialiazation
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.') #Lets print this for confirmation for now


display = []
for letter in chosen_word:
    display.append("_")
print(display)

#Use a while loop to let the user guess again until all the letters of the word have been guessed
#Print they have won

end_of_game = False
while not end_of_game: #Was stuck on this while loop condition for 2 days💔
    guess = input("Guess a letter: ").lower()


    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess #I told you my method would save the day
    print(display)
    
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1    
    if lives == 0:
        end_of_game = True
        print("You lose")


    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    # if lives == 6:
    #     print(stages[6])
    # elif lives == 5:
    #     print(stages[5])
    # elif lives == 4:
    #     print(stages[4])
    # elif lives == 3:
    #     print(stages[3])
    # elif lives == 2:
    #     print(stages[2])
    # elif lives == 1:
    #     print(stages[1])
    # elif lives == 0:
    #     print(stages[0])  #I literally just waffled in this whole part

    #This is a better thing to do
    print(stages[lives])