class Book:
    def __init__(self, title, author, copies=1):
        if copies < 0:
            raise ValueError("Copies cannot be negative.")
        self.title = title.strip()
        self.author = author.strip()
        self.__copies = copies

    def get_copies(self):
        return self.__copies

    def add_copies(self, count=1):
        if count < 1:
            raise ValueError("Count must be positive.")
        self.__copies += count

    def borrow(self):
        if self.__copies == 0:
            return False
        self.__copies -= 1
        return True

    def return_book(self):
        self.__copies += 1

    def __str__(self):
        return f"'{self.title}' by {self.author} — {self.__copies} copies"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, copies=1):
        key = title.strip().casefold()
        if key in self.books:
            self.books[key].add_copies(copies)
            print("Book already exists; copy count increased.")
        else:
            self.books[key] = Book(title, author, copies)
            print("Book added.")

    def show_books(self):
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books.values():
            print(book)

    def borrow_book(self, title):
        book = self.books.get(title.strip().casefold())
        if book is None:
            print("Book not found.")
        elif not book.borrow():
            print("No copies are available.")
        else:
            print("Book borrowed successfully.")

    def return_book(self, title):
        book = self.books.get(title.strip().casefold())
        if book is None:
            print("Book not found.")
        else:
            book.return_book()
            print("Book returned successfully.")


if __name__ == "__main__":
    library = Library()
    while True:
        print("\\n1. Add book  2. Show books  3. Borrow  4. Return  5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            copies = int(input("Number of copies: "))
            library.add_book(title, author, copies)
        elif choice == "2":
            library.show_books()
        elif choice == "3":
            library.borrow_book(input("Title to borrow: "))
        elif choice == "4":
            library.return_book(input("Title to return: "))
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
