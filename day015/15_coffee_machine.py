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
    "coffee": 200,
}


def check_resources(drink: dict):
    """Check the resources and return False if it is not enough"""
    for k in drink:
        if drink.get(k) > resources.get(k):
            print(f"Sorry there is not enough {k}.")
            return False
        else:
            return True


def coins():
    """Ask user how many coins he pay and returns the total calculated from coins inserted."""
    quarters = float(input("how many quarters(0.25$)?: "))
    dimes = float(input("how many dimes(0.10$)?: "))
    nickles = float(input("how many nickles(0.05$)?: "))
    pennies = float(input("how many pennies(0.01$)?: "))
    return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)


def deduct_resources(drink: dict):
    """Deducted resources after makes drink"""
    for res in drink:
        resources[res] -= drink[res]


def make_coffee(money):
    on = True

    while on:
        users_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if users_choice == "off":
            on = False
            break
        elif users_choice == "report":
            print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
        else:
            drink = MENU[users_choice]["ingredients"]
            price = MENU[users_choice]["cost"]
            if not check_resources(drink):
                continue
            print("Please insert coins.")
            user_coins = coins()
            if user_coins < price:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                change = round(user_coins - price, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {users_choice}. Enjoy!")
            money += price
            deduct_resources(drink)


make_coffee(money=0)


# TODO: 1. Create a main function that check users input and decides what to do next

# TODO: 2. Create the flag that ends program when the user enter "off"

# TODO: 3. Create the report function that return current resources values

# TODO: 4. After user coffee choice make function which check resources(water, milk and coffee.
#  If some is less than it need not continue to make the drink but print: “Sorry there is not enough water.”

# TODO: 5. After the program prompt the user to insert coins.
#  Check that the user has inserted enough money to purchase the drink

# TODO: 6. If user enter enough money, machine should make coffee and give change

# TODO: 7. After program should deducted from the coffee machine resources