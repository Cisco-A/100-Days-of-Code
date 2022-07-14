MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffeeIngredients(coffee_type):
    water = MENU[coffee_type]["ingredients"]["water"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    # cost = MENU[coffee_type]["cost"]

    if coffee_type == "espresso":
        milk = 0
    else:
        milk = MENU[coffee_type]["ingredients"]["milk"]

    if resources["water"] < water:
        return f"There isn't enough water"
    elif resources["milk"] < milk:
        return f"There isn't enough milk"
    elif resources["coffee"] < coffee:
        return f"There isn't enough coffee"
    else:
        return "Proceed"


def deductResources(coffee_type):
    """Deduct the resource needed to make a coffee from the resources bank"""
    water = MENU[coffee_type]["ingredients"]["water"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    # cost = MENU[coffee_type]["cost"]

    if coffee_type == "espresso":
        milk = 0
    else:
        milk = MENU[coffee_type]["ingredients"]["milk"]

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee



resources["profit"] = 0
turnOff = False
while not turnOff:
    # Printouts
    order = input("What would you like to have? espresso/latte/cappuccino? ").lower()

    if order != "off" and order != "report":
        print(coffeeIngredients(order))
    elif order == "off":
        turnOff = True
    elif order == "report":
        print(resources)

    if order != "off" and order != "report":
        # noinspection PySimplifyBooleanCheck
        if coffeeIngredients(order) == "Proceed":
            # Prompt for money in form of coins
            print("INSERT COINS")
            penny = int(input("Penny: ")) * 0.01
            nickel = int(input("Nickel: ")) * 0.05
            dime = int(input("Dime: ")) * 0.10
            quarter = int(input("Quarter: ")) * 0.25


            dollar = penny + nickel + dime + quarter

            # Deduct resources and add cost
            coffeeCost = MENU[order]["cost"]
            if coffeeCost > dollar:
                print(f"Sorry, you do not have enough coins. Here is your ${dollar}")
            elif coffeeCost == dollar:
                deductResources(order)
                resources["profit"] += coffeeCost
                print(f"Enjoy your {order}.")
            else:
                deductResources(order)
                resources["profit"] += coffeeCost
                print(f"Enjoy your {order}.")
                change = round(dollar - coffeeCost, 2)
                print(f"Here is your change: ${change}")

print("Thank you for using this machine.")
