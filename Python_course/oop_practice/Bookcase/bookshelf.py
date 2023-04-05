from book import Book


class Shelf:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add(self, book: Book) -> None:
        """add book obj"""
        self.books.append(book)

    def get(self, name: str) -> Book:
        """return book obj"""
        if name in self.books:
            return self.books[self.books.index(name)]

    def remove(self, name: str):
        """remove book"""
        if name in self.books:
            return self.books.remove(name)

