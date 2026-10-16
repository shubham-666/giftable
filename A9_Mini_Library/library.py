import csv
import json
from pathlib import Path
from book import Book


class Library:
    def __init__(self):
        self.books = {}

    @staticmethod
    def _key(title):
        return title.strip().casefold()

    def add_book(self, title, author, copies=1):
        key = self._key(title)
        if key in self.books:
            self.books[key].add_copies(copies)
        else:
            self.books[key] = Book(title, author, copies)

    def show_books(self):
        if not self.books:
            print("Library is empty.")
        for book in self.books.values():
            print(book)

    def borrow_book(self, title):
        book = self.books.get(self._key(title))
        if book is None:
            print("Book not found.")
            return False
        if not book.borrow():
            print("No copies available.")
            return False
        print("Book borrowed.")
        return True

    def return_book(self, title):
        book = self.books.get(self._key(title))
        if book is None:
            print("Book not found.")
            return False
        book.return_book()
        print("Book returned.")
        return True

    def save_json(self, filename="library.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books.values()], file, indent=4)

    def load_json(self, filename="library.json"):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("JSON must contain a list of books.")
            loaded = {}
            for item in data:
                book = Book(item["title"], item["author"], int(item["copies"]))
                loaded[self._key(book.title)] = book
            self.books = loaded
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print("Could not load library:", error)

    def export_csv(self, filename="library.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "author", "copies"])
            writer.writeheader()
            for book in self.books.values():
                writer.writerow(book.to_dict())

    def read_text_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                print(file.read(), end="")
        except FileNotFoundError:
            print(f"File not found: {filename}")
