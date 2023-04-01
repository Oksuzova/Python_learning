from bookshelves import Bookshelves


class UnReadBooks(Bookshelves):

    def __init__(self):
        super().__init__()
        self.num_of_books = 0
        self.book = {}

    def get_book_data(self):
        return self.book

    def put_book(self, autor, name):
        self.book = {autor: name}
        self.num_of_books += 1

    def del_book(self, autor):
        self.book.pop(autor)
        self.num_of_books -= 1
