from bookshelves import Bookshelves
from book import Book


class ReadBooks(Bookshelves):

    def __init__(self):
        super().__init__()
        self.book = {}

    def get_book_data(self):
        return self.book

    def put_book(self, autor, name):
        self.book = {autor: name}
