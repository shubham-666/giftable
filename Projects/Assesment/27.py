file_path = r"C:\Users\DELL\Downloads\agenticAI\student.txt"


while True:

    print("\n===== STUDENT MENU =====")
    print("1. Write")
    print("2. Read")
    print("3. Update")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # WRITE
    if choice == "1":

        n = int(input("How many students do you want to write? "))

        with open(file_path, "a") as file:

            for i in range(n):
                name = input(f"Enter student {i + 1} name: ")
                file.write(name + "\n")

        print(f"{n} student(s) added successfully.")


    # READ
    elif choice == "2":

        n = int(input("How many students do you want to read? "))

        try:
            with open(file_path, "r") as file:
                students = file.readlines()

            total = len(students)

            if total == 0:
                print("No students found.")
                continue

            n = min(n, total)

            print("\nStudent Names:")

            for i in range(n):
                print(f"{i + 1}. {students[i].strip()}")

        except FileNotFoundError:
            print("File does not exist.")


    # UPDATE
    elif choice == "3":

        try:
            with open(file_path, "r") as file:
                students = file.readlines()

            if len(students) == 0:
                print("No students found.")
                continue

            print("\nCurrent Students:")

            for i, name in enumerate(students, start=1):
                print(f"{i}. {name.strip()}")

            n = int(input("\nHow many students do you want to update? "))

            for i in range(n):

                number = int(input("Enter student number to update: "))

                if 1 <= number <= len(students):

                    new_name = input("Enter new student name: ")

                    students[number - 1] = new_name + "\n"

                else:
                    print("Invalid student number.")

            with open(file_path, "w") as file:
                file.writelines(students)

            print(f"{n} student(s) updated successfully.")

        except FileNotFoundError:
            print("File does not exist.")


    # EXIT
    elif choice == "4":

        print("Program ended.")
        break


    else:
        print("Invalid choice.")





import json
subject = {"python", "pasing_marks": }




#Assignment: in library program- save data to CSV and add exception.