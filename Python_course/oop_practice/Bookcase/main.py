from bookshelves import Bookshelves
from read_books import ReadBooks
from unread_books import UnReadBooks
from book import Book

read_book = ReadBooks()
unread_book = UnReadBooks()
bookshelf = Bookshelves()

book1 = Book(name="Harry Potter", autor="J.K. Rolling")

unread_book.put_book(name=book1.name, autor=book1.autor)
print(unread_book.book)
print(unread_book.num_of_books)
print(bookshelf.num_of_books)
