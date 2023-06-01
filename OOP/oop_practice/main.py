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


class A:
    def __init__(self):
        self.a = 3
        self.b = 7
        self.c = 3

    def __repr__(self):
        return self.__class__.__name__

class B(A):
    def __init__(self):
        self.a = 2
        self.b = 0
        self.c = 2

class C(A):
    def __init__(self):
        self.a = 4
        self.b = 2
        self.c = 4


class Manager:
    _l = []
    def set_data(self, *arg):
        self._l.extend(arg)

    def sort_by(self, attr: str = None):
        print(sorted(self._l, key=lambda x: getattr(x, attr)))

m = Manager()
m.set_data(C(), A(), B())
m.sort_by('a')
m.sort_by('b')







