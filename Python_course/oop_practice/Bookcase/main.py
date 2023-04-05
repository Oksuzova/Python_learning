from book_manager import Closet
from bookshelf import Shelf
from book import Book

# read_book = ReadBooks()
# unread_book = UnReadBooks()
# bookshelf = Bookshelves()

book1 = Book(name="Harry Potter", author="J.K. Rolling")
book2 = Book(name="Pride and Prejudice", author="Jane Austen")
book3 = Book(name="1984", author="George Orwell")


closet = Closet()

closet.take(book1)
closet.take(book2)

print(f"Count unread books: {closet.count_unread()}")
print(f"Count read books: {closet.count_read()}")
print(f"Total count books: {closet.total()}")

print("Read book1\n...")
closet.reading(book1)

print(f"Count unread books: {closet.count_unread()}")
print(f"Count read books: {closet.count_read()}")
print(f"Total count books: {closet.total()}")

print("Read book1\n...")
closet.reading(book2)

print(f"Count unread books: {closet.count_unread()}")
print(f"Count read books: {closet.count_read()}")
print(f"Total count books: {closet.total()}")

print("Take book3\n...")
closet.take(book3)

print(f"Count unread books: {closet.count_unread()}")
print(f"Count read books: {closet.count_read()}")
print(f"Total count books: {closet.total()}")

print("Retrieve book1\n...")
closet.retrieve(book1)

print(f"Count unread books: {closet.count_unread()}")
print(f"Count read books: {closet.count_read()}")
print(f"Total count books: {closet.total()}")

print(closet)

print(book2.read)


