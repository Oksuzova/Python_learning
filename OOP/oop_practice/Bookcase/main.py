from book_manager import Closet
from bookshelf import Shelf
from book import Book


book1 = Book(name="Harry Potter", author="J.K. Rolling")
book2 = Book(name="Pride and Prejudice", author="Jane Austen")
book3 = Book(name="1984", author="George Orwell")

closet = Closet()

closet.take(book1.name, book1.author)
closet.take(book2.name, book2.author)

print(f"Count unread books: {closet.count_unread}")
print(f"Count read books: {closet.count_read}")
print(f"Total count books: {closet.total}")

print("Read book1\n...")
closet.reading(book1.name)

print(f"Count unread books: {closet.count_unread}")
print(f"Count read books: {closet.count_read}")
print(f"Total count books: {closet.total}")

print("Read book2\n...")
closet.reading(book2.name)

print(f"Count unread books: {closet.count_unread}")
print(f"Count read books: {closet.count_read}")
print(f"Total count books: {closet.total}")

print("Take book3\n...")
closet.take(book3.name, book3.author)

print(f"Count unread books: {closet.count_unread}")
print(f"Count read books: {closet.count_read}")
print(f"Total count books: {closet.total}")

print("Retrieve book1\n...")
closet.retrieve(book1.name)

print(f"Count unread books: {closet.count_unread}")
print(f"Count read books: {closet.count_read}")
print(f"Total count books: {closet.total}")

print(closet)

print(isinstance(book1, str))


