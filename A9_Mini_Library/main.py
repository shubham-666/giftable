from library import Library


def main():
    library = Library()
    while True:
        print("\\n=== Mini Library ===")
        print("1. Add book")
        print("2. Show books")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Save to JSON")
        print("6. Load from JSON")
        print("7. Export CSV")
        print("8. Read a text file")
        print("9. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                copies = int(input("Copies to add: "))
                library.add_book(title, author, copies)
                print("Book saved in memory.")
            elif choice == "2":
                library.show_books()
            elif choice == "3":
                library.borrow_book(input("Title to borrow: "))
            elif choice == "4":
                library.return_book(input("Title to return: "))
            elif choice == "5":
                library.save_json()
                print("Saved to library.json.")
            elif choice == "6":
                library.load_json()
            elif choice == "7":
                library.export_csv()
                print("Exported to library.csv.")
            elif choice == "8":
                library.read_text_file(input("Text filename: ").strip())
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Choose a number from 1 to 9.")
        except (ValueError, OSError) as error:
            print("Operation failed:", error)


if __name__ == "__main__":
    main()
