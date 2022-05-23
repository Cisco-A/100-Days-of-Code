#bankers Roulette
import random

names_string = input("Give me everybody's name, seperated by a comma. ")
names = names_string.split(", ")

#Get the total number of items in the list and add to the random function
length = len(names)

#1 is subtracted from the length because index starts counting at 0
#and the length returns the list number counted from 1 not 0
rando = random.randint(0, length - 1)

person_paying = names[rando]

print(f"{person_paying} is paying for our meals.")