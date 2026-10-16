MY_NAME = "Shubham Tiwari"

import csv
import json


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if value < 0 or value > 100:
            print("Marks should be between 0 and 100.")
        else:
            self.__marks = value

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 40:
            return "C"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.name} - Marks: {self.__marks}, Grade: {self.grade()}"


student1 = Student(MY_NAME, 85)
student2 = Student("Ravi", 72)
student3 = Student("Priya", 38)

students = [student1, student2, student3]


# -----------------------------
# C1 - TEXT FILE
# -----------------------------

with open("students.txt", "w") as file:
    for student in students:
        file.write(student.name + "," + str(student.get_marks()) + "\n")


print("TEXT FILE:")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


# -----------------------------
# C2 - CSV FILE
# -----------------------------

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "marks"])

    for student in students:
        writer.writerow([student.name, student.get_marks()])


print("\nCSV FILE:")

with open("students.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# -----------------------------
# C3 - JSON FILE
# -----------------------------

student_data = []

for student in students:
    data = {
        "name": student.name,
        "marks": student.get_marks(),
        "grade": student.grade()
    }

    student_data.append(data)


with open("students.json", "w") as file:
    json.dump(student_data, file, indent=4)


print("\nJSON FILE:")

with open("students.json", "r") as file:
    data = json.load(file)

    for student in data:
        print(student["name"], "-", student["grade"])