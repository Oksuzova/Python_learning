from Washing_mode import WashingMode


class Resources:
    wash = WashingMode()

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

    def check_resources(self, user_input):
        if self.mode_resources[user_input]["washing powder"] <= self.resources["washing powder"]:
            if self.mode_resources[user_input]["conditioner"] <= self.resources["conditioner"]:
                return True

    def wash_process(self, user_input: str, with_drying: bool):
        self.resources["washing powder"] -= self.mode_resources[user_input]["washing powder"]
        self.resources["conditioner"] -= self.mode_resources[user_input]["conditioner"]
        if with_drying:
            price = self.wash.get_costs(user_input)
        else:
            price = self.wash.mode[user_input]['costs']
        self.resources["money"] += price

    def waiting_process(self, user_input: str):
        min_left = int(self.wash.get_time(user_input))
        while min_left > 0:
            min_left -= int(input("How many minutes have passed? "))
            print(f"{min_left} min left")
        print("Your clothes are ready")
