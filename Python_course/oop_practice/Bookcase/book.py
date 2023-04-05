from __future__ import annotations
from typing import Union


class Book:

    def __init__(self, name, author, read=False):
        self.name = name
        self.author = author
        self.read = read

    def get_name(self) -> str:
        return self.name

    def get_author(self) -> str:
        return self.author

    def set_read(self) -> None:
        self.read = True

    def is_read(self) -> bool:
        return self.read

    def __eq__(self, other: Union[str, Book]):
        if isinstance(other, str):
            return self.get_name().lower() == other.lower()
        if isinstance(other, Book):
            return self.get_name().lower() == other.get_name().lower()

    def __str__(self):
        return f"Author: {self.author}, Name: {self.name}"
