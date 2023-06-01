import unittest
from book import Book
from bookshelf import Shelf
from book_manager import Closet


name = "Name"
author = "Author"
shelf_name = "Bookshelf"


class TestBook(unittest.TestCase):

    def setUp(self):
        self.book = Book(name=name, author=author, read=True)

    def test_get_name(self):
        self.assertEqual(self.book.get_name(), name)

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), author)

    def test_read(self):
        self.assertEqual(self.book.read, True)

    def test_read_setter(self):
        self.book.read = False
        self.assertEqual(self.book.read, False)

    def test_read_default_false(self):
        book = Book(name=name, author=author)
        self.assertEqual(book.read, False)


class TestBookshelf(unittest.TestCase):

    def setUp(self):
        self.book = Book(name=name, author=author, read=True)
        self.shelf = Shelf(shelf_name)
        print("Something SetUp")

    @classmethod
    def setUpClass(cls) -> None:
        print("Something SetUpClass")

    def test_add(self):
        self.shelf.add(self.book)
        self.assertEqual(len(self.shelf), 1)
        self.assertEqual(self.shelf.books, [self.book])

    def test_get(self):
        self.shelf.add(self.book)
        self.assertEqual(self.shelf.get(name), self.book)

    def test_remove(self):
        self.shelf.add(self.book)
        self.assertEqual(self.shelf.remove(name), self.book)
        self.assertEqual(len(self.shelf), 0, msg="Book was removed, but still present")


class TestBookManager(unittest.TestCase):

    def setUp(self):
        self.closet = Closet()

    def test_take(self):
        book = Book(name=name, author=author)
        self.assertEqual(self.closet.take(name=book.name, author=book.author), book)
        self.assertEqual(len(self.closet.no_read), 1, msg="Book was taken, but still present")
        self.assertEqual(self.closet.count_unread, 1, msg="Book was taken, but still present")

    def test_reading(self):
        book = self.closet.take(name=name, author=author)
        self.assertEqual(self.closet.reading(book.name), None, msg="None wasn`t return")
        self.assertTrue(book.read, msg="Book wasn`t read state")
        self.assertEqual(self.closet.count_unread, 0, msg="Book wasn`t deleted from unread shelf")
        self.assertEqual(self.closet.count_read, 1, msg="Book wasn`t add to read shelf")

    def test_reading_raise_error(self):
        book = self.closet.take(name=name, author=author)

        with self.assertRaises(AssertionError):
            assert 1 == 2
           # self.assertEqual(self.closet.reading("abc"), None, msg="None wasn`t return")

        self.assertFalse(book.read, msg="Book wasn`t read state")
        self.assertEqual(self.closet.count_read, 0, msg="Book wasn`t add to read shelf")
        self.assertEqual(self.closet.count_unread, 1, msg="Book wasn`t add to read shelf")

    def test_retrieve(self):
        book = Book(name=name, author=author)
        self.assertEqual(self.closet.retrieve(book.name), None, msg="None wasn`t return")
        self.closet.read.add(book)
        self.assertEqual(self.closet.retrieve(book.name), book, msg="Book wasn`t return")
        self.assertEqual(self.closet.count_unread, 0, msg="Book was returned, but still present in unread shelf")
        self.closet.no_read.add(book)
        self.assertEqual(self.closet.retrieve(book.name), book, msg="Book wasn`t return")
        self.assertEqual(self.closet.count_read, 0, msg="Book was returned, but still present in read shelf")

    def test_count_unread(self):
        book = Book(name=name, author=author)
        self.assertEqual(self.closet.count_unread, 0, msg="Does not return 0, if unread shelf is empty")
        self.closet.no_read.add(book)
        self.assertEqual(self.closet.count_unread, 1, msg="Does not return 1, if unread shelf len is 1")

    def test_count_read(self):
        book = Book(name=name, author=author)
        self.assertEqual(self.closet.count_read, 0, msg="Does not return 0, if read shelf is empty")
        self.closet.read.add(book)
        self.assertEqual(self.closet.count_read, 1, msg="Does not return 1, if read shelf len is 1")

    def test_total(self):
        book = Book(name=name, author=author)
        self.assertEqual(self.closet.total, 0, msg="Does not return 0, if bookshelf is empty")
        self.closet.no_read.add(book)
        self.closet.read.add(book)
        self.assertEqual(self.closet.total, 2, msg="Does not return correct count of total books in bookshelf")


# if __name__ == "__main__":
#     unittest.main()

