class Book:

    def __init__(self, autor, name):
        self.autor = autor
        self.name = name
        self.is_read = False

    def reading(self):
        self.is_read = True
