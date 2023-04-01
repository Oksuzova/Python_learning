from Washing_mode import WashingMode


class CheckPayment:

    wash = WashingMode()

    def check_money(self, deposit: float, with_drying: bool, user_input: str):
        if with_drying:
            price = self.wash.get_costs(user_input)
        else:
            price = self.wash.mode[user_input]['costs']
        if deposit >= price:
            print(f"Your change is {deposit - price} $")
            return True
        return False
