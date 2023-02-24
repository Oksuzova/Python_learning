from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
make_coffee = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    users_input = input(f"What would you like? ({menu.get_items()})?: ")
    if users_input == "off":
        on = False
        break
    elif users_input == "report":
        make_coffee.report()
        money.report()
    elif users_input in menu.get_items():
        order = menu.find_drink(users_input)
        if make_coffee.is_resource_sufficient(order):
            if money.make_payment(order.cost) == 0:
                print("Invalid data. Try again")
            else:
                make_coffee.make_coffee(order)
    else:
        print("Invalid data. Try again")
