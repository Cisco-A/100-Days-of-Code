# Higher or Lower
import random
from data import data



print("Welcome to the HIGHER or LOWER game!")


def textFormat(random_char):
    name = random_char["name"]
    description = random_char["description"]
    country = random_char["country"]

    return f"{name}, a {description} from {country}. Count is {random_char['follower_count']}"


random_1 = random.choice(data)

# Looping until right user loses
score = 0
correct = True
while correct:

    random_2 = random.choice(data)
    if random_2 == random_1:
        random_2 = random.choice(data)

    print(f"Compare A: {textFormat(random_1)}")
    print(f"Against B: {textFormat(random_2)}")


    guess = input("Who has the highest follower count? A or B: ").upper()


    # Comparing count to determine if user is wrong or not
    if guess == "A":
        if random_1["follower_count"] > random_2["follower_count"]:
            score += 1
            print(f"Your current score: {score}")
            random_1 = random_2
        else:
            correct = False
            print("You lose")
    elif guess == "B":
        if random_2["follower_count"] > random_1["follower_count"]:
            score += 1
            print(f"Your current score: {score}")
            random_1 = random_2
        else:
            correct = False
            print("You lose")



# TODO 8: Finalize and run the full program
