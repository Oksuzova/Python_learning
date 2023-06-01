from teapot import Teapot


class TeapotManager:

    def __init__(self):
        self.teapot = Teapot()

    def turn_on(self):
        if self.check_teapot_state():
            self.teapot.is_enable = True

    def turn_off(self):
        self.teapot.is_enable = False

    def ten_min_later(self):
        self.teapot.water_temp = True
        self.turn_off()

    def pour_water(self):
        self.teapot.water = True

    def make_coffee(self):
        if self.teapot.water and self.teapot.water_temp:
            self.teapot.water = False
            self.teapot.water_temp = False
            print("Here is your coffee")
        else:
            print("You can`t do it. Check the teapot state.")

    def check_teapot_state(self):
        if self.teapot.water:
            if not self.teapot.water_temp:
                return True
            else:
                print("Water already hot")
        else:
            print("Not enough water")

    def __str__(self):
        return f"{self.teapot.get_water()}\n{self.teapot.get_water_state()}\n{self.teapot.get_is_enable()}"
