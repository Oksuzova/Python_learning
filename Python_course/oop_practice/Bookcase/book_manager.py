from book import Book
from bookshelf import Shelf


class Closet:

    def __init__(self):
        self.read = Shelf('Was read')
        self.no_read = Shelf('Will read')

    def take(self, book: Book):
        """ add new book as unread"""
        self.no_read.add(book)

    def reading(self, book: Book):
        """ read the book"""
        self.no_read.remove(book.name)
        self.read.add(book)
        book.set_read()

    def retrieve(self, book: Book):
        """return book to library (move from closet)"""
        self.no_read.remove(book.name)
        self.read.remove(book.name)

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
