import unittest
from book import Book


class TestBook(unittest.TestCase):

    def setUp(self):
        name = "Name"
        author = "Author"
        self.book = Book(name=name, author=author)

    def test_get_name(self):
        self.assertEqual(self.book.get_name(), "Name")

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), "Author")

    def test_read(self):
        self.assertEqual(self.book.read, False)

    def test_read_setter(self):
        self.book.read = True
        self.assertEqual(self.book.read, True)


if __name__ == "__main__":
    unittest.main()






