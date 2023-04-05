class FirstClass:

    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


# n1 = FirstClass()
# n1.setdata(1)
# n1.setdata(2)
# n1.display()
#
# n1.another_name = "spam"
# print(n1.another_name)

class SecondClass(FirstClass):
    def display(self):
        print(f"Current value = {self.data}")


n2 = SecondClass()
n2.setdata(42)
n2.display()

print(n2)  # <__main__.SecondClass object at 0x000001BAF6130450>


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return f"[ThirdClass: {self.data}]"

    def mul(self, other):
        self.data *= other


a = ThirdClass("abc")
a.display() # "Current value = "abc"
print(a) # [ThirdClass: abc]

b = a + "xyz"
b.display() # Current value = abcxyz

print(b) # [ThirdClass: abcxyz]

a.mul(3)
print(a) # [ThirdClass: abcabcabc]






