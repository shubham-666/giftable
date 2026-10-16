MY_NAME = "Shubham Tiwari"


def read_marks_file(filename):
    try:
        with open(filename, "r") as file:
            marks = file.read().strip()

        marks = int(marks)

        print("Marks:", marks)

    except FileNotFoundError:
        print("File not found:", filename)

    except ValueError:
        print("The contents of", filename, "were not a number.")

    finally:
        print("File operation finished.")


# Create a file containing hello
with open("hello_marks.txt", "w") as file:
    file.write("hello")


# Create a file containing 75
with open("good_marks.txt", "w") as file:
    file.write("75")


print("1. Missing file")
read_marks_file("missing_marks.txt")

print("\n2. File containing hello")
read_marks_file("hello_marks.txt")

print("\n3. File containing 75")
read_marks_file("good_marks.txt")