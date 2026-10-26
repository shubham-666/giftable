
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class BookRequest(BaseModel):
    bookName: str
    NoOfCopies: int = Field(gt=0)


inventory = {
    "wings of fire": 2
}


def normalize_name(name: str) -> str:
    return name.strip().lower()


@app.get("/library")
def get_library_books():
    return inventory


@app.get("/library/{bookName}")
def get_library(bookName: str):
    name = normalize_name(bookName)

    if name not in inventory:
        raise HTTPException(status_code=404, detail="Book not found")

    return {
        "bookName": name,
        "available_copies": inventory[name]
    }


@app.post("/library")
def add_book(book: BookRequest):
    name = normalize_name(book.bookName)

    inventory[name] = inventory.get(name, 0) + book.NoOfCopies

    return {
        "message": "Book added successfully",
        "bookName": name,
        "total_copies": inventory[name]
    }


@app.post("/library_borrow")
def borrow_book(book_name: str):
    name = normalize_name(book_name)

    if name not in inventory:
        raise HTTPException(status_code=404, detail="Book not found")

    if inventory[name] <= 0:
        raise HTTPException(status_code=400, detail="No copies available")

    inventory[name] -= 1

    return {
        "message": "Book borrowed successfully",
        "bookName": name,
        "remaining_copies": inventory[name]
    }


@app.put("/library/{bookName}")
def update_book(bookName: str, book: BookRequest):
    name = normalize_name(bookName)

    if name not in inventory:
        raise HTTPException(status_code=404, detail="Book not found")

    if normalize_name(book.bookName) != name:
        raise HTTPException(
            status_code=400,
            detail="Book name in the body must match the URL"
        )

    inventory[name] = book.NoOfCopies

    return {
        "message": "Book copies updated successfully",
        "bookName": name,
        "total_copies": inventory[name]
    }


@app.delete("/library/{bookName}")
def delete_book(bookName: str):
    name = normalize_name(bookName)

    if name not in inventory:
        raise HTTPException(status_code=404, detail="Book not found")

    del inventory[name]

    return {
        "message": "Book and all its copies deleted successfully",
        "bookName": name
    }
