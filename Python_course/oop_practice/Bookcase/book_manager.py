from book import Book
from bookshelf import Shelf


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
        if name in self.no_read.books:
            book = self.no_read.books[self.no_read.books.index(name)]
            self.no_read.remove(book.name)
            self.read.add(book)
            book.set_read()
        return None

    def retrieve(self, name: str) -> Book:
        """return book to library (move from closet)"""
        if name in self.no_read.books:
            book = self.no_read.books[self.no_read.books.index(name)]
            self.no_read.remove(book.name)
            return book
        if name in self.read.books:
            book = self.read.books[self.read.books.index(name)]
            self.read.remove(book.name)
            return book


    def total(self) -> int:
        """get number of all the books"""
        total = len(self.no_read.books) + len(self.read.books)
        return total

    def count_unread(self) -> int:
        """get number of unread books"""
        return len(self.no_read.books)

    def count_read(self) -> int:
        """get number of read books"""
        return len(self.read.books)

    def __str__(self):
        """<return two list with names of books>"""
        unread_books = ""
        for num in range(len(self.no_read.books)):
            unread_books += str(f"{self.no_read.books[num]}; ")
        read_books = ""
        for num in range(len(self.read.books)):
            read_books += str(f"{self.read.books[num]}; ")
        return f"Unread books : {unread_books}\nRead books: {read_books}"
