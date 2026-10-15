def read_number_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            value = file.read().strip()
        number = int(value)
        print("Number read:", number)
    except FileNotFoundError:
        print("Error: file was not found.")
    except ValueError:
        print("Error: file does not contain a valid integer.")
    finally:
        print("File operation finished.")


if __name__ == "__main__":
    # Run each case by entering the requested filename:
    # 1) a missing filename, e.g. missing.txt
    # 2) a file containing non-numeric text
    # 3) a file containing a valid integer
    filename = input("Enter filename to read: ").strip()
    read_number_from_file(filename)
