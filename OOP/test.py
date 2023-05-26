# -*- coding: cp1251 -*-1

class ListNode:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def get_prev(self):
        return self.prev

    def set_prev(self, p):
        self.prev = p

    def set_data(self, d):
        self.data = d

    def get_data(self, key=None):
        if key is None:
            return self.data
        else:
            return self.data[key]


class DoubleList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.insidelist = []
        self.x = None

    def add(self, data):
        if data is None:
            return False
        else:
            if data not in self.insidelist:
                new_node = ListNode(data, None, None)
                self.insidelist.append(data)
                self.size += 1
                if self.head is None:
                    self.head = self.tail = new_node
                else:
                    new_node.prev = self.tail
                    new_node.next = None
                    self.tail.next = new_node
                    self.tail = new_node
            else:
                print("Element {0} is already in set".format(data))
                return False
        return True

    def addAll(self, *args):
        trigger = 0
        if args is None:
            return False
        else:
            for i in args:
                if i not in self.insidelist:
                    new_node = ListNode(i, None, None)
                    self.insidelist.append(i)
                    self.size += 1
                    trigger += 1
                    if self.head is None:
                        self.head = self.tail = new_node
                    else:
                        new_node.prev = self.tail
                        new_node.next = None
                        self.tail.next = new_node
                        self.tail = new_node
                else:
                    print("Element {0} is already in set".format(i))
        if trigger == 0:
            return False
        return True

    def remove(self, node_value=None):
        if node_value is None:
            return False
        current_node = self.head
        if node_value in self.insidelist:
            while current_node is not None:
                if current_node.data == node_value:
                    self.size -= 1
                    self.insidelist.remove(node_value)
                    if current_node.prev is not None and current_node.next is not None:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    else:
                        if current_node.next is not None:
                            self.head = current_node.next
                            current_node.next.prev = None
                        else:
                            self.tail = current_node.prev
                            current_node.prev.next = None
                current_node = current_node.next
        else:
            print("Element {0} not in set".format(node_value))
            return False
        return self.insidelist

    def removeAll(self, *args):
        trigger = 0
        if args is None:
            return False
        else:
            for i in args:
                current_node = self.head
                if i in self.insidelist:
                    while current_node is not None:
                        if current_node.data == i:
                            self.size -= 1
                            self.insidelist.remove(i)
                            trigger += 1
                            if current_node.prev is not None and current_node.next is not None:
                                current_node.prev.next = current_node.next
                                current_node.next.prev = current_node.prev
                            else:
                                if current_node.next is not None:
                                    self.head = current_node.next
                                    current_node.next.prev = None
                                else:
                                    self.tail = current_node.prev
                                    current_node.prev.next = None
                        current_node = current_node.next
                else:
                    print("Element {0} not in set".format(i))
        if trigger == 0:
            return False
        return self.insidelist

    def clearAll(self):
        current_node = self.head
        self.insidelist.clear()
        while current_node is not None:
            self.size -= 1
            if current_node.prev is None:
                if current_node.next is not None:
                    self.head = current_node.next
                    current_node.next.prev = None
                else:
                    self.head = self.tail = None
            current_node = current_node.next
        return True

    # Вивід множини двома способами
    def show(self, n=None):
        if n is None:
            n = input("Show style : \n" + "1 --> for short view \n" +
                      "2 --> for detailed view\n" + "Your choose: ")
        if int(n) == 1:
            container = []
            current_node = self.head
            while current_node is not None:
                container.append(current_node.data)
                current_node = current_node.next
            print(" <--> ".join([str(i) for i in container]))
        elif int(n) == 2:
            print("Show list data:")
            current_node = self.head
            while current_node is not None:
                print("prev : {0} , current : {1} , next : {2}".format(current_node.prev.data
                                                                       if hasattr(current_node.prev, "data") else None,
                                                                       current_node.data,
                                                                       current_node.next.data if hasattr(
                                                                           current_node.next, "data") else None))
                current_node = current_node.next
            print("*" * 50)

    def size(self):
        return str(self.size)

    def equals(self, *args):
        if args is None:
            return False
        if len(args) == self.size:
            for i in args:
                if i in self.insidelist:
                    continue
                else:
                    print("Not equal")
                    return False
        else:
            print("Not equal")
            return False
        return True

    # повертає множину у вигляді массиву

    def toArray(self):
        return self.insidelist

    # повертає True якщо поточна множина порожня
    # в іншому випадку повертає False

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    # повертає True якщо поточна множина містить
    # елемент  переданий у функцію,
    # в іншому випадку повертає False

    def contains(self, data=None):
        if data is None:
            return False
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    # повертає True якщо поточна множина містить
    # усі елементи множини переданої у функцію,
    # в іншому випадку повертає False

    def containsAll(self, *args):
        if len(args) == 0:
            return False
        num = 0
        for data in args:
            current_node = self.head
            while current_node:
                if current_node.data == data:
                    num += 1
                    break
                else:
                    current_node = current_node.next

        if len(args) == num:
            return True
        else:
            return False

    # видаляє з поточної множини елементи яких немає у множині,
    # що передається в якості параметра
    # повертає True якщо поточна множина була змінена
    # False якщо не була змінена

    def retainAll(self, *args):
        if len(args) == 0 or self.size == 0:
            return False
        using = [i for i in args]
        for f in using:
            if f not in self.insidelist:
                using.remove(f)
                if len(using) == 0:
                    return False
        current_node = self.head
        trigger = 0
        for i in range(self.size):
            while current_node is not None:
                if current_node.data in using:
                    break
                else:
                    trigger = 1
                    self.remove(current_node.data)
                    break
            current_node = current_node.next
        return True if trigger == 1 else False

    def info(self):
        print("--size() : int <- return size of list \n"
              "--isEmpty() : boolean <- return True if list is empty, False if else \n"
              "--contains(obj) : boolean <- return True if element inside list, False if else \n"
              "--toArray() : list <- transform to built in type list \n"
              "--add(obj) : boolean <- add element to list \n"
              "--remove(obj) : None <- remove element from list \n"
              "--addAll(list) : boolean <- add list of items \n"
              "--removeAll(list) : boolean <- remove list of elements \n"
              "--containsAll(list) : boolean <- return True if list of elements, False if else\n"
              "--retainAll(list) : boolean <- return True if list was changed, False if else \n"
              "------------------- removes elements from current set if they are not in func \n"
              "--clear() : None <- remove all elements from list \n"
              "--equals(list) : boolean <- True if current set is equal to set in func \n")

    def __getitem__(self, index):
        if index > self.size - 1:
            raise IndexError
        current_node = self.head
        while index != 0:
            current_node = current_node.next
            index -= 1
        return current_node

    def __setitem__(self, index, value):
        if index > self.size or index < 0:
            raise IndexError
        if value is None or value in self.insidelist:
            raise AttributeError
        if index == 0 and self.head is not None:
            self.size += 1
            current_node = self.head
            new_node = ListNode(value, None, None)
            current_node.prev = new_node
            new_node.next = current_node
            new_node.prev = None
            self.head = new_node
        elif index == 0 and self.head is None:
            self.size += 1
            self.head = self.tail = ListNode(value, None, None)
        else:
            previous_node = self.__getitem__(index - 1)
            current_node = self.__getitem__(index)
            new_node = ListNode(value, None, None)
            current_node.prev = new_node
            previous_node.next = new_node
            new_node.next = current_node
            new_node.prev = previous_node
            self.size += 1

    def list_sort(self, key, param=None, reverse=False):
        if param is not None:
            was_swap = True
            while was_swap:
                was_swap = False
                if reverse == False:
                    for i in range(key.size - 1):
                        if key[i].get_data(param) > key[i + 1].get_data(param):
                            key[i].data, key[i + 1].data = key[i + 1].data, key[i].data
                            was_swap = True
                elif reverse == True:
                    for i in range(key.size - 1):
                        if key[i].get_data(param) < key[i + 1].get_data(param):
                            key[i].data, key[i + 1].data = key[i + 1].data, key[i].data
                            was_swap = True
                else:
                    raise AttributeError
        else:
            was_swap = True
            while was_swap:
                was_swap = False
                if reverse == False:
                    for i in range(key.size - 1):
                        if key[i].data > key[i + 1].data:
                            key[i].data, key[i + 1].data = key[i + 1].data, key[i].data
                            was_swap = True
                elif reverse == True:
                    for i in range(key.size - 1):
                        if key[i].data < key[i + 1].data:
                            key[i].data, key[i + 1].data = key[i + 1].data, key[i].data
                            was_swap = True
                else:
                    raise AttributeError


# myList = DoubleList()
# myList.addAll(3, 4, 6, 7, 5, 2, 1)
# myList[5] = 0
# myList.show(2)
# myList.list_sort(myList)
# myList.show(2)

from lab_6 import *

l = Microwave(200, 220)
l1 = Microwave(350, 350)
l2 = Microwave(150, 120)
l3 = Fridge(250, 450)
r = Fridge(450, 800)
r1 = Fridge(250, 700)
r2 = WashingMachine(125, 745)
t = WashingMachine(300, 850)
t1 = Laptop(900, 625)
i = Laptop(1000, 800)
i1 = Laptop(1200, 950)
First_pack = DoubleList()
First_pack.addAll(l, l1, l2, l3, r, r1)
First_pack.list_sort(First_pack, "power")
First_pack.show(1)
Second_pack = DoubleList()
Third_pack = DoubleList()
Third_pack.addAll(i1, r2, l)
Third_pack.show(1)
Third_pack.remove(i1)
Third_pack.show(1)

# class A:
#     def __init__(self):
#         self.a = 3
#         self.b = 7
#         self.c = 3
#
#     def __repr__(self):
#         return self.__class__.__name__
#
# class B(A):
#     def __init__(self):
#         self.a = 2
#         self.b = 0
#         self.c = 2
#
# class C(A):
#     def __init__(self):
#         self.a = 4
#         self.b = 2
#         self.c = 4
#
#
# class Manager:
#     _l = []
#     def set_data(self, *arg):
#         self._l.extend(arg)
#
#     def sort_by(self, attr: str = None):
#         print(sorted(self._l, key=lambda x: getattr(x, attr)))
#
# m = Manager()
# m.set_data(C(), A(), B())
# m.sort_by('a')
# m.sort_by('b')
