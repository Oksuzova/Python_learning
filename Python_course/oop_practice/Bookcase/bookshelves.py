class Bookshelves:

    def __init__(self):
        self.num_of_books = 0

    def get_num_books(self):
        return self.num_of_books

    def put_book(self, autor, name):
        self.num_of_books += 1

    def del_book(self, autor):
        self.num_of_books -= 1
