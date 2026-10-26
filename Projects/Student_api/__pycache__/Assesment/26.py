class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book, copies):
        if book.title in self.books:
            self.books[book.title]["total"] += copies
            self.books[book.title]["available"] += copies
        else:
            self.books[book.title] = {
                "book": book,
                "total": copies,
                "available": copies
            }

    def show_books(self):
        print(f"\nLibrary: {self.name}")

        if not self.books:
            print("No books available.")
            return

        for title, details in self.books.items():
            print(
                f"Title: {title}, "
                f"Author: {details['book'].author}, "
                f"Total Copies: {details['total']}, "
                f"Available: {details['available']}"
            )

    def borrow_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif self.books[title]["available"] == 0:
            print("No copy available.")
        else:
            self.books[title]["available"] -= 1
            print(f"You borrowed '{title}'.")

    def return_book(self, title):
        if title not in self.books:
            print("Book not found.")
        elif self.books[title]["available"] == self.books[title]["total"]:
            print("No borrowed copy exists.")
        else:
            self.books[title]["available"] += 1
            print(f"You returned '{title}'.")


# Number of libraries
number_of_libraries = int(input("Enter number of libraries: "))

libraries = []

for i in range(number_of_libraries):
    name = input(f"\nEnter name of library {i + 1}: ")
    libraries.append(Library(name))


while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nSelect Library:")

        for i, library in enumerate(libraries):
            print(f"{i + 1}. {library.name}")

        library_number = int(input("Enter library number: "))
        library = libraries[library_number - 1]

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        copies = int(input("Enter number of copies: "))

        book = Book(title, author)
        library.add_book(book, copies)

        print("Book added successfully.")

    elif choice == 2:
        for library in libraries:
            library.show_books()

    elif choice == 3:
        print("\nSelect Library:")

        for i, library in enumerate(libraries):
            print(f"{i + 1}. {library.name}")

        library_number = int(input("Enter library number: "))
        library = libraries[library_number - 1]

        title = input("Enter book title to borrow: ")
        library.borrow_book(title)

    elif choice == 4:
        print("\nSelect Library:")

        for i, library in enumerate(libraries):
            print(f"{i + 1}. {library.name}")

        library_number = int(input("Enter library number: "))
        library = libraries[library_number - 1]

        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")