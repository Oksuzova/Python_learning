from book import Book


class Shelf:

    def __init__(self, name):
        self.name = name
        self.books = []

    def get(self, name: str) -> Book:
        """return book obj"""
        if name in self.books:
            return self.books[self.books.index(name)]

    def add(self, book: Book) -> None:
        """add book obj"""
        self.books.append(book)

    def remove(self, name: str):
        """remove book"""
        if name in self.books:
            return self.books.pop(self.books.index(name))

    def __len__(self):
        return len(self.books)
