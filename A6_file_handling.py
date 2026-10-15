import csv
import json

names_input = input("Enter student names separated by commas: ")
names = [name.strip() for name in names_input.split(",") if name.strip()]

# Plain text: one name per line
with open("students.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\\n")

with open("students.txt", "r", encoding="utf-8") as file:
    print("\\nNames read from students.txt:")
    print(file.read(), end="")

# CSV with DictWriter and DictReader
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name"])
    writer.writeheader()
    for name in names:
        writer.writerow({"name": name})

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\\nNames read from students.csv:")
    for row in reader:
        print(row["name"])

# JSON with dump and load
student_data = {"students": names}
with open("students.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, indent=4)

with open("students.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("\\nNames read from students.json:")
for name in loaded_data["students"]:
    print(name)
