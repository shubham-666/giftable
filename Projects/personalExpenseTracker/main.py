
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from pathlib import Path

app = FastAPI(title="Personal Expense Tracker")

BASE_DIR = Path(__file__).resolve().parent

# Store expenses in a dictionary
expenses = {}
next_id = 1


class Expense(BaseModel):
    description: str = Field(min_length=1)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1)


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


@app.post("/expenses")
def add_expense(expense: Expense):
    global next_id

    description = expense.description.strip()
    category = expense.category.strip()

    if not description or not category:
        raise HTTPException(
            status_code=400,
            detail="Description and category cannot be empty"
        )

    expense_id = next_id
    next_id += 1

    expenses[expense_id] = {
        "id": expense_id,
        "description": description,
        "amount": expense.amount,
        "category": category
    }

    return {
        "message": "Expense added successfully",
        "expense": expenses[expense_id]
    }


@app.get("/expenses")
def get_expenses():
    return {
        "expenses": list(expenses.values()),
        "total": round(sum(e["amount"] for e in expenses.values()), 2)
    }


@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    if expense_id not in expenses:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    description = expense.description.strip()
    category = expense.category.strip()

    if not description or not category:
        raise HTTPException(
            status_code=400,
            detail="Description and category cannot be empty"
        )

    expenses[expense_id] = {
        "id": expense_id,
        "description": description,
        "amount": expense.amount,
        "category": category
    }

    return {
        "message": "Expense updated successfully",
        "expense": expenses[expense_id]
    }


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    if expense_id not in expenses:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    deleted = expenses.pop(expense_id)

    return {
        "message": "Expense deleted successfully",
        "expense": deleted
    }
