class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = None
        self.set_marks(marks)

    def set_marks(self, marks):
        if not isinstance(marks, (int, float)) or not 0 <= marks <= 100:
            print("Invalid marks: enter a value from 0 to 100.")
            return False
        self.__marks = marks
        return True

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.__marks}"


if __name__ == "__main__":
    your_name = input("Enter your name: ").strip() or "Student"
    students = [
        Student(your_name, float(input(f"Enter marks for {your_name}: "))),
        Student(input("Enter second student's name: ").strip(), float(input("Enter second student's marks: "))),
        Student(input("Enter third student's name: ").strip(), float(input("Enter third student's marks: "))),
    ]

    print("\\nStudent details:")
    for student in students:
        print(student)

    print("\\nTesting validation by trying to set 150:")
    students[0].set_marks(150)
    print("Marks remain:", students[0].get_marks())
