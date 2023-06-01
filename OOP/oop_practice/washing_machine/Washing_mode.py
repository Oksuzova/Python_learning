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

    def with_drying(self, with_drying: bool, user_input: str):
        if with_drying:
            print(f"You choose {user_input} with drying washing mode.\n"
                  f"Waiting time: {self.get_time(user_input)} min.\n"
                  f"Costs: {self.get_costs(user_input)} $")
        else:
            print(f"You choose {user_input} without drying washing mode.\n"
                  f"Waiting time: {self.mode[user_input]['time']} min.\n"
                  f"Costs: {self.mode[user_input]['costs']} $")
