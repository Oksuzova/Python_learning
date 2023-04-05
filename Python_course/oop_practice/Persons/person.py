class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    #  Adding Methods to Encapsulate Operations to Improve Maintainability
    def lastname(self):
        return self.name.split()[-1]

    # @rangetest(percent=(0.0, 1.0))
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return f"Person: {self.name} {self.pay}"


class Manager(Person):

    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)

    def give_raise(self, percent, bonus=.10):
        # self.pay = int(self.pay * (1 + percent + bonus)) - bad way
        Person.give_raise(self, percent + bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)


    def add_members(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)



if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job='dev', pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

    # print(bob.name.split()[-1])
    # sue.pay *= 10
    # print(sue.pay)

    print(bob.lastname(), sue.lastname()) # bob.lastname(), sue.lastname() ->
                                          # <bound method Person.lastname of
                                          # <__main__.Person object at 0x000002284A71C190>> Jones

    sue.give_raise(.10)
    print(sue.pay)

    # bob.give_raise(.10)
    # print(bob.pay)

    print(sue)
    print(bob)

    tom = Manager("Tom Jones", 50000)

# Manager: __init__
    tom.give_raise(.10)
    print(tom.lastname())
    print(tom)

    # print("--All three--")
    # for obj in (bob, sue, tom):
    #     obj.give_raise(.10)
    #     print(obj)



    development = Department(bob, sue)
    # development.add_members(tom)
    # development.give_raises(.10)
    development.show_all()
    print(development.members)





