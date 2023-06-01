class Soda:

    def __init__(self, additive=None):
        self.add = additive

    def show_my_drink(self):
        if self.add:
            print(f"soda and {self.add}")
        else:
            print("just soda")


my_soda = Soda("topping")
my_soda.show_my_drink()

my_friend_soda = Soda()
my_friend_soda.show_my_drink()
