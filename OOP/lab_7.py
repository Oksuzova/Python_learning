# Oksuzova T. io-z21
nzk = 2108
c2 = nzk % 2  # 0 => list
c3 = nzk % 3  # 2 => Doubly linked list

from lab_6 import *

class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return self.item.__class__.__name__


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.current = None
        self.list_items = []

    def update_items(self, data):
        if len(self.list_items) != 0:
            self.list_items.clear()
            self.start_node = None
            self.end_node = None
            self.current = None

        for item in data:
            new_node = Node(item)
            self.list_items.append(new_node)
            if self.start_node is None:
                self.start_node = self.end_node = new_node
            else:
                new_node.prev = self.end_node
                new_node.next = None
                self.end_node.next = new_node
                self.end_node = new_node
        self.current = self.start_node

    def add_in_emptylist(self, data):
        if self.start_node is None:
            for item in data:
                new_node = Node(item)
                self.list_items.append(new_node)
                if self.start_node is None:
                    self.start_node = self.end_node = new_node
                else:
                    new_node.prev = self.end_node
                    new_node.next = None
                    self.end_node.next = new_node
                    self.end_node = new_node
                self.current = self.start_node
        else:
            print("Sorry, list is not empty.")

    def select_next_item(self):
        if self.current.next is None:
            print("Next item does not exist")
        else:
            self.current = self.current.next

    def select_prev_item(self):
        if self.current.prev is None:
            print("Previous item does not exist")
        else:
            self.current = self.current.prev

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node
        self.list_items.insert(0, new_node)

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        self.list_items.insert(len(self.list_items) + 1, new_node)

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
                if n.next is not None:
                    n.next.prev = new_node
                n.next = new_node
                self.list_items.insert(self.list_items.index(n) + 1, new_node)

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node
                self.list_items.insert(self.list_items.index(n) - 1, new_node)

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.next is not None:
            if n.item == x:
                break
            n = n.next
        self.list_items.remove(n)
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.item == x:
                n.prev.next = None
            else:
                print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.list_items.reverse()
        self.start_node = p

    def __repr__(self):
        string = ""
        for item in self.list_items:
            if self.current == item:
                string += f"[{item}], "
            else:
                string += f"{item}, "
        return f"[{string[:-2]}]"


def main():

    # ---------------------------------CREATING INSTANSE--------------------------------------------------------------#

    m = Microwave(5, 2)
    l = Laptop(2, 4)
    f = Fridge(3, 6, enable=True)
    w = WashingMachine(3, 5, enable=True)

    m2 = Microwave(50, 20)
    l2 = Laptop(20, 40)
    f2 = Fridge(30, 60)
    w2 = WashingMachine(30, 50)

    # ---------------------------------CREATING COLLECTION-----------------------------------------------------------#

    device = DeviceManager()
    device.set_items(m, l, f, w)

    # ------------------------------------CREATING LIST--------------------------------------------------------------#

    double_linked_list = DoublyLinkedList()
    double_linked_list.add_in_emptylist(device.get_items())
    print(double_linked_list)

    # -----------------------------------SORT LIST-------------------------------------------------------------------#

    sort = device.sort_by_ascending("Power")
    double_linked_list.update_items(sort)
    print(double_linked_list)

    # ----------------------------------SELECTING ITEMS--------------------------------------------------------------#

    double_linked_list.select_prev_item()
    print(double_linked_list)

    double_linked_list.select_next_item()
    print(double_linked_list)

    double_linked_list.select_prev_item()
    print(double_linked_list)

    # ----------------------------------OPERATIONS ITEMS--------------------------------------------------------------#

    double_linked_list.insert_at_start(m2)
    print(double_linked_list)

    double_linked_list.insert_at_end(l2)
    print(double_linked_list)

    double_linked_list.insert_after_item(w, f2)
    print(double_linked_list)

    double_linked_list.insert_before_item(w, w2)
    print(double_linked_list)

    double_linked_list.delete_element_by_value(w2)
    print(double_linked_list)

    double_linked_list.select_next_item()
    double_linked_list.select_next_item()
    double_linked_list.select_next_item()
    print(double_linked_list)



if __name__ == '__main__':
    main()

