class Teapot:

    def __init__(self, water=False, water_temp=False, is_enable=False):
        self.water = water
        self.water_temp = water_temp
        self.is_enable = is_enable

    def get_water(self):
        if self.water:
            return "Water: is enough"
        else:
            return "Water: is not enough"

    def get_water_state(self):
        if self.water_temp:
            return "Water: is boiled"
        else:
            return "Water: is unboiled"

    def get_is_enable(self):
        if self.is_enable:
            return "Teapot: is on"
        else:
            return "Teapot: is off"

