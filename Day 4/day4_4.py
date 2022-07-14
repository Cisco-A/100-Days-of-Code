#A rock-paper-scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors  "))

game_images = [rock , paper, scissors]

#Toavoid an index error, pass this statement as so
if choice >= 3 or choice <= 0:
    print("You made an invalid entry you lose!")
else:
    print("You")
    print(game_images[choice])

    print("Computer:")

    #Computer
    comp_choice = random.randint(0, 2)
    print(game_images[comp_choice])

    #Winning Algo

    if choice == 0 and comp_choice == 1:
        print("Computer wins")
    elif choice == 1 and comp_choice == 0:
        print("You win")
    elif choice == 1 and comp_choice == 2:
        print("Computer wins")
    elif choice == 2 and comp_choice == 1:
        print("You win")
    elif choice == 0 and comp_choice == 2:
        print("Computer wins")
    elif choice == 2 and comp_choice == 0:
        print("You win")
    elif choice == comp_choice:
        print("It is a draw")