from book import Book
from bookshelf import Shelf
from typing import Union


class Closet:

    def __init__(self):
        self.read = Shelf('Was read')
        self.no_read = Shelf('Will read')

    def take(self, name, author) -> Book:
        """ add new book as unread"""
        book = Book(name=name, author=author)
        self.no_read.add(book)
        return book

    def reading(self, name: str) -> None:
        """ read the book"""
        book = self.no_read.remove(name)
        if book:
            book.read = True
            self.read.add(book)
        else:
            raise ValueError(f"Book with name {name} is not found in shelf {self.no_read.name}.")

    def retrieve(self, name: str) -> Union[Book, None]:
        """return book to library (move from closet)"""
        book = self.no_read.remove(name) or self.read.remove(name)
        if book:
            return book
        else:
            print(f"Book with name {name} is not found in bookshelf.")

    @property
    def count_unread(self) -> int:
        """get number of unread books"""
        return len(self.no_read)

    @property
    def count_read(self) -> int:
        """get number of read books"""
        return len(self.read)

    @property
    def total(self) -> int:
        """get number of all the books"""
        total = len(self.no_read) + len(self.read)
        return total

    def __str__(self):
        """<return two list with names of books>"""
        unread_books = "; ".join(str(x) for x in self.no_read.books)
        read_books = "; ".join(str(x) for x in self.read.books)
        return f"Unread books : {unread_books}\nRead books: {read_books}"
