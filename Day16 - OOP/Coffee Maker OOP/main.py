from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_off = False
menu = Menu()

make_coffee = CoffeeMaker()
money = MoneyMachine()
while not turn_off:
    order = input(f"What would you like to have? ({menu.get_items()}): ").lower()

    if order == "off":
        turn_off = True
    elif order == "report":
        make_coffee.report()
    if make_coffee.is_resource_sufficient(order):





