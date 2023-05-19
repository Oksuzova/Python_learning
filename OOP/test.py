# -*- coding: cp1251 -*-1

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


