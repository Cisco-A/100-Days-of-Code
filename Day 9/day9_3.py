# A blind bidding program

# Initialization

persons = {}
highest_bid = 0
winner = ""
end_of_input = False
while not end_of_input:
    name_input = input("What is your name? ")
    bid_input = int(input("What's your bid? "))
    persons[name_input] = bid_input
    another_bidder = input("Is there another bidder? ")

    if another_bidder == "no":
        end_of_input = True


for key in persons:
    if persons[key] > highest_bid:
        highest_bid = persons[key]
        winner = key
print(f"The highest bidder is {winner}")