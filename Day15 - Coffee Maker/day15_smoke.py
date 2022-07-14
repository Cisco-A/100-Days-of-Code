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

order = input("What would you like to have? espresso/latte/cappuccino? ")


# print("INSERT COINS")
# penny = int(input("Penny: ")) * 0.01
# nickel = int(input("Nickel: ")) * 0.05
# dime = int(input("Dime: ")) * 0.10
# quarter = int(input("Quarter: ")) * 0.25

# Coffee Processor
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
    if resources["milk"] < milk:
        return f"There isn't enough milk"
    if resources["coffee"] < coffee:
        return f"There isn't enough coffee"


# Checking resources


# Process coins
def processCoins(penny_amount, nickel_amount, dime_amount, quarter_amount):
    dollar = 0
    return dollar + penny_amount + nickel_amount + dime_amount + quarter_amount


# Transaction
def transaction():
    pass

