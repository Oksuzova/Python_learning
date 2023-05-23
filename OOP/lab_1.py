# Oksuzova T. io-z21

class First:
    def __init__(self):
        self.nzk = 2108
        self.c2 = self.nzk % 2      # 0 => O1 == +
        self.c3 = self.nzk % 3      # 2 => O2 == /
        self.c5 = self.nzk % 5      # 3 => C == 5
        self.c7 = self.nzk % 7      # 1 => i, j = short (int)

        self.c = self.c5
        self.n = 10
        self.m = 2
        self.a = 4
        self.b = 2

        self.s = 0

    def calculations(self):
        if self.a <= -self.c <= self.n or self.b <= 0 <= self.m:
            print("Division by zero")
            return
        for i in range(self.a, self.n + 1):
            for j in range(self.b, self.m + 1):
                self.s += (i / j) / (i + self.c)
        print(self.s)


def main():
    first = First()
    first.calculations()


if __name__ == '__main__':
    main()

