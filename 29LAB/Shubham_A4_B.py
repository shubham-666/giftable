MY_NAME = "Shubham Tiwari"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def set_marks(self, value):
        if value < 0 or value > 100:
            print("Marks should be between 0 and 100.")
        else:
            self.__marks = value
            print("Marks updated.")

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


print(student1)
print(student2)
print(student3)


print("\nTrying to give 150 marks to", student1.name)
student1.set_marks(150)

print("Old marks:", student1.get_marks())
print(student1)