class WashingMode:
    def __init__(self):
        self.mode = {
            "daily": {
                "time": 120,
                "costs": 1,
            },
            "delicate": {
                "time": 40,
                "costs": 1.5,
            },
            "white": {
                "time": 60,
                "costs": 2,
            },
        }

        self.dop_mode = {
            "drying": {
                "time": 10,
                "costs": 0.5,
            },
        }

    def get_mode(self):
        modes = ""
        for mode in self.mode:
            modes += f"{mode}/"
        return modes

    def get_time(self, user_input: str):
        time = int(self.mode[user_input]["time"] + self.dop_mode["drying"]["time"])
        return time

    def get_costs(self, user_input: str):
        cost = self.mode[user_input]["costs"] + self.dop_mode["drying"]["costs"]
        return cost

    def with_drying(self):
        print(f"You choose {user_input} with drying washing mode.\n"
              f"Waiting time: {wash.get_time(user_input)} min.\n"
              f"Costs: {wash.get_costs(user_input)} $")

    def without_drying(self):
        print(f"You choose {user_input} without drying washing mode.\n"
              f"Waiting time: {self.mode[user_input]['time']} min.\n"
              f"Costs: {self.mode[user_input]['costs']} $")


class Resources:
    def __init__(self):

        self.mode_resources = {
            "daily": {
                "washing powder": 100,
                "conditioner": 30,
            },
            "delicate": {
                "washing powder": 50,
                "conditioner": 70,
            },
            "white": {
                "washing powder": 100,
                "conditioner": 50,
            },
        }

        self.resources = {
            "washing powder": 200,
            "conditioner": 100,
            "money": 0,
        }

    def report(self):
        print(f"washing powder: {self.resources['washing powder']}\n"
              f"conditioner: {self.resources['conditioner']}\n"
              f"money: {self.resources['money']}")

    def wash_process(self, user_input: str, with_drying: bool):
        self.resources["washing powder"] -= self.mode_resources[user_input]["washing powder"]
        self.resources["conditioner"] -= self.mode_resources[user_input]["conditioner"]
        if with_drying:
            price = wash.get_costs(user_input)
        else:
            price = wash.mode[user_input]['costs']
        self.resources["money"] += price

    def waiting_process(self, user_input: str):
        min_left = int(wash.get_time(user_input))
        while min_left > 0:
            min_left -= int(input("How many minutes have passed? "))
            print(f"{min_left} min left")
        print("Your clothes are ready")


class CheckPayment:

    def check_money(self, deposit: float, with_drying: bool):
        if with_drying:
            price = wash.get_costs(user_input)
        else:
            price = wash.mode[user_input]['costs']
        if deposit >= price:
            print(f"Your change is {deposit - price} $")
            return True
        return False


wash = WashingMode()
resource = Resources()
money = CheckPayment()

with_drying = True
on = True

while on:
    user_input = input(f"Washing machine is ready. Please, choose mode {wash.get_mode()}: ")
    if user_input == "off":
        on = False
    elif user_input in wash.get_mode():
        drying = input("If you need drying? Enter 'yes' or 'not': ")
        if drying == "yes":
            wash.with_drying()
        else:
            wash.without_drying()

        print("If it correct, please enter money.")
        deposit = float(input("How much money did you deposit?: "))
        if money.check_money(deposit, with_drying):
            print("Washing machine is working. Please wait...")
            resource.wash_process(user_input, with_drying)
            resource.waiting_process(user_input)
        else:
            print("Not enough money")

    elif user_input == "report":
        resource.report()

    else:
        print("Please, enter correct mode.")

