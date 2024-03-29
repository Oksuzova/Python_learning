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

money = 0


def check_resources(drink: dict):
    """Check the resources and return False if it is not enough."""
    drink = drink["ingredients"]
    for k in drink:
        if drink.get(k) > resources.get(k):
            print(f"Sorry there is not enough {k}.")
            return False
        else:
            return True


def coins():
    """Ask user how many coins he pay and returns the total calculated from coins inserted."""
    flag = True
    while flag:
        try:
            quarters = int(input("how many quarters(0.25$)?: "))
            dimes = int(input("how many dimes(0.10$)?: "))
            nickles = int(input("how many nickles(0.05$)?: "))
            pennies = int(input("how many pennies(0.01$)?: "))
            flag = False
            return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
        except:
            print("You enter invalid data. Try again ")


def deduct_resources(drink: dict):
    """Deducted resources after makes drink."""
    drink = drink["ingredients"]
    for res in drink:
        resources[res] -= drink[res]


def make_coffee(drink: dict):
    price = drink["cost"]
    if not check_resources(drink):
        return 0
    print("Please insert coins.")
    user_coins = coins()
    if user_coins < price:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        change = round(user_coins - price, 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {users_choice}. Enjoy!")
    deduct_resources(drink)


on = True

while on:
    users_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if users_choice == "off":
        on = False
        break
    elif users_choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    elif users_choice == "latte" or users_choice == "espresso" or users_choice == "cappuccino":
        drink = MENU[users_choice]
        check = make_coffee(drink)
        if check != 0:
            money += drink["cost"]
    else:
        print("Invalid data. Try again")


# TODO: 1. Create a main function that check users input and decides what to do next

# TODO: 2. Create the flag that ends program when the user enter "off"

# TODO: 3. Create the report function that return current resources values

# TODO: 4. After user coffee choice make function which check resources(water, milk and coffee.
#  If some is less than it need not continue to make the drink but print: “Sorry there is not enough water.”

# TODO: 5. After the program prompt the user to insert coins.
#  Check that the user has inserted enough money to purchase the drink

# TODO: 6. If user enter enough money, machine should make coffee and give change

# TODO: 7. After program should deducted from the coffee machine resources
