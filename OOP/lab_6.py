# -*- coding: cp1251 -*-1

# Oksuzova T. io-z21
nzk = 2108
c11 = nzk % 13  # 2 => Determine the hierarchy of electrical appliances.
                    # Plug in some electrical appliances. Calculate the power consumption.
                    # Sort appliances in the apartment based on power.
                    # Find a device in the apartment that corresponds to the given range of electro-magnetic radiation.

class Device:
    def __init__(self, power: int, e_m_radiation: int, enable=False):
        self._power = power
        self._e_m_radiation = e_m_radiation
        self.enable = enable
        self.name = "Device"

    def state(self):
        if self.enable:
            return "Enable"
        else:
            return "Disable"

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, v):
        self._power = v

    @property
    def e_m_radiation(self):
        return self._e_m_radiation

    @e_m_radiation.setter
    def e_m_radiation(self, v):
        self._e_m_radiation = v

    def set_state(self, v):
        self.enable = v

    def __str__(self):
        return f"Device: {self.name}, Power: {self.power} W, " \
               f"Electro-magnetic radiation: {self.e_m_radiation} µW/cm2, state: {self.state()}"

    def __repr__(self):
        return self.__class__.__name__


class Microwave(Device):
    def __init__(self, power: int, e_m_radiation: int, enable=False):
        super().__init__(power, e_m_radiation, enable)
        self.name = "Microwave"


class WashingMachine(Device):
    def __init__(self, power: int, e_m_radiation: int, enable=False):
        Device.__init__(self, power, e_m_radiation, enable)
        self.name = "Washing Machine"


class Fridge(Device):
    def __init__(self, power: int, e_m_radiation: int, enable=False):
        Device.__init__(self, power, e_m_radiation, enable)
        self.name = "Fridge"


class Laptop(Device):
    def __init__(self, power: int, e_m_radiation: int, enable=False):
        Device.__init__(self, power, e_m_radiation, enable)
        self.name = "Laptop"


class DeviceManager:
    def __init__(self):
        self.items = []

    def set_items(self, *args):
        self.items.extend(args)

    def get_items(self):
        return self.items

    def sort_by_ascending(self, attr: str = None):
        return sorted(self.items, key=lambda x: getattr(x, attr.lower()))

    def sort_by_descending(self, attr: str = None):
        return sorted(self.items, key=lambda x: getattr(x, attr.lower()), reverse=True)

    @property
    def current_power(self):
        return sum(x.power for x in self.items if x.enable)

    def check_radiation(self, r_min: int, r_max: int):
        devices = []
        for i in self.items:
            if r_min <= i.e_m_radiation <= r_max:
                devices.append(i)
        return None if len(devices) == 0 else devices

def main():

    m = Microwave(5, 2)
    l = Laptop(2, 4)
    f = Fridge(3, 6, enable=True)
    w = WashingMachine(3, 5, enable=True)
    m.set_state(True)

    print(l)
    print(m)
    print(f)
    print(w)

    manager = DeviceManager()
    manager.set_items(m, l, f, w)

    print(manager.sort_by_ascending("Power"))
    print(manager.current_power)

    print(manager.check_radiation(0, 5))

if __name__ == '__main__':
    main()



