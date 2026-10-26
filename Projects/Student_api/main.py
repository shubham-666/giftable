
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import os

app = FastAPI()

CSV_FILE = "students.csv"


class Student(BaseModel):
    id: int
    name: str
    course: str


students = {
    1: {"name": "Abhi", "course": "Java"},
    2: {"name": "Riya", "course": "Python"},
    3: {"name": "Deepak More", "course": "System Design"},
}


def save_students():
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["studentId", "name", "course"])

        for student_id, details in students.items():
            writer.writerow([
                student_id,
                details["name"],
                details["course"]
            ])


def load_students():
    loaded_students = {}

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student_id = int(row["studentId"])
            loaded_students[student_id] = {
                "name": row["name"],
                "course": row["course"]
            }

    return loaded_students


# Load existing data, or create the CSV with initial students.
if os.path.exists(CSV_FILE) and os.path.getsize(CSV_FILE) > 0:
    students = load_students()
else:
    save_students()


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"id": student_id, **students[student_id]}


@app.post("/students", status_code=201)
def add_student(student: Student):
    if student.id in students:
        raise HTTPException(
            status_code=409,
            detail="Student ID already exists"
        )

    students[student.id] = {
        "name": student.name,
        "course": student.course
    }

    save_students()

    return {"id": student.id, **students[student.id]}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    removed = students.pop(student_id)
    save_students()

    return {
        "message": "Student deleted successfully",
        "deleted": {"id": student_id, **removed}
    }


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if student.id != student_id:
        raise HTTPException(
            status_code=400,
            detail="Student ID in the body must match the URL"
        )

    students[student_id] = {
        "name": student.name,
        "course": student.course
    }

    save_students()

    return {"id": student_id, **students[student_id]}
