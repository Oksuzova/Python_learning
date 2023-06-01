from __future__ import annotations
from typing import Union


class Book:

    def __init__(self, name, author, read=False):
        self.name = name
        self.author = author
        self._read = read

    def get_name(self) -> str:
        return self.name

    def get_author(self) -> str:
        return self.author

    @property
    def read(self) -> bool:
        return self._read

    @read.setter
    def read(self, value) -> None:
        self._read = value

    def __eq__(self, other: Union[str, Book]):
        if isinstance(other, str):
            return self.get_name().lower() == other.lower()
        if isinstance(other, Book):
            return self.get_name().lower() == other.get_name().lower()

    def __str__(self):
        return f"Author: {self.author}, Name: {self.name}"
