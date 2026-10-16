import csv
import json

students = []
for i in range(3):
    name = input(f"Enter student {i + 1} name: ").strip()
    marks = float(input(f"Enter {name}'s marks: "))
    students.append({"name": name, "marks": marks})

with open("students.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write(f"{student['name']}: {student['marks']}\\n")

with open("students.txt", "r", encoding="utf-8") as file:
    print("\\nTEXT FILE")
    print(file.read(), end="")

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "marks"])
    writer.writeheader()
    writer.writerows(students)

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    print("\\nCSV FILE")
    for row in csv.DictReader(file):
        print(row)

with open("students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    print("\\nJSON FILE")
    print(json.load(file))
