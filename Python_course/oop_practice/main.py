class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


n1 = FirstClass()
n1.setdata(1)
n1.setdata(2)
n1.display()

n1.another_name = "spam"
print(n1.another_name)
