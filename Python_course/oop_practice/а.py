class Color:

    def __init__(self, color=None):
        self.color = color


class Light(Color):

    def __init__(self, color):
        self.enabled = False
        super().__init__(color)

    def state(self, enable):
        self.enabled = enable

    def __str__(self):
        return f'<{self.color} is {"enable" if self.enabled else "disable"}>'

    def __repr__(self):
        return f'<{self.color} is {"enable" if self.enabled else "disable"}>'


class TraficLight:

    def __init__(self):
        self.green = Light('green')
        self.yellow = Light('yellow')
        self.red = Light('red')

    def run(self):
        self.green.state(True)
        self.yellow.state(False)
        self.red.state(False)

    def stopp(self):
        self.green.state(False)
        self.yellow.state(False)
        self.red.state(True)

    def __str__(self):
        return f'{self.green}\n{self.yellow}\n{self.red}\n'

    def __repr__(self):
        return f'{self.green}\n{self.yellow}\n{self.red}\n'


t = TraficLight()
print(t)
t.stopp()
print(t)
t.run()
print(t)