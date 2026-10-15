import tempfile
from pathlib import Path
from book import Book
from library import Library


def check(condition, message):
    if not condition:
        raise AssertionError(message)
    print("PASS:", message)


def main():
    book = Book("Python", "A. Author", 1)
    check(book.copies == 1, "Book stores its initial copy count")
    check(book.borrow() is True, "Borrow succeeds when a copy is available")
    check(book.copies == 0, "Borrow reduces copies")
    check(book.borrow() is False, "Borrow refuses when no copies remain")

    library = Library()
    library.add_book("Python", "A. Author", 1)
    library.add_book("Python", "A. Author", 2)
    check(len(library.books) == 1, "Adding the same title does not duplicate it")
    check(library.books["python"].copies == 3, "Adding existing title increases copies")

    with tempfile.TemporaryDirectory() as temp_dir:
        json_path = Path(temp_dir) / "library.json"
        csv_path = Path(temp_dir) / "library.csv"
        library.save_json(str(json_path))
        loaded = Library()
        loaded.load_json(str(json_path))
        check("python" in loaded.books, "JSON save and load work")
        loaded.export_csv(str(csv_path))
        check(csv_path.exists() and csv_path.stat().st_size > 0, "CSV export creates a file")

    print("All green")


if __name__ == "__main__":
    main()
