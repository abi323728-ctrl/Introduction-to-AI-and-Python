"""
Project: 05_personal_expense_tracker.py
Description: A professional console-based Personal Expense Tracker with category tagging,
             budget monitoring, summary reports, and JSON-based file persistence.
Module: Module 02 - Python Mini Projects
"""

import json
import os
from datetime import datetime

DATA_FILE = "expenses_data.json"

CATEGORIES = ["Food & Dining", "Transportation", "Utilities", "Entertainment", "Education", "Healthcare", "Other"]

def load_expenses() -> list[dict]:
    """Loads expenses from JSON file or returns empty list if file doesn't exist."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []
    return []

def save_expenses(expenses: list[dict]):
    """Persists expenses list into JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=4)
    except IOError as e:
        print(f"[Error saving data]: {e}")

def add_expense(expenses: list[dict], title: str, amount: float, category: str) -> dict:
    """Adds a new expense entry with timestamp."""
    if category not in CATEGORIES:
        category = "Other"
    
    entry = {
        "id": len(expenses) + 1,
        "title": title.strip(),
        "amount": round(float(amount), 2),
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(entry)
    save_expenses(expenses)
    return entry

def generate_expense_summary(expenses: list[dict], monthly_budget: float = 1000.0) -> dict:
    """Generates detailed financial metrics and category breakdowns."""
    total_spent = sum(item["amount"] for item in expenses)
    remaining_budget = monthly_budget - total_spent
    
    category_totals = {cat: 0.0 for cat in CATEGORIES}
    for item in expenses:
        cat = item.get("category", "Other")
        category_totals[cat] = category_totals.get(cat, 0.0) + item["amount"]
    
    return {
        "total_spent": total_spent,
        "monthly_budget": monthly_budget,
        "remaining_budget": remaining_budget,
        "budget_used_percentage": (total_spent / monthly_budget * 100) if monthly_budget > 0 else 0.0,
        "category_breakdown": category_totals
    }

def print_expense_report(expenses: list[dict], monthly_budget: float = 1000.0):
    """Prints a structured financial report to the terminal."""
    summary = generate_expense_summary(expenses, monthly_budget)
    
    print("\n" + "=" * 70)
    print("                    PERSONAL EXPENSE REPORT                          ")
    print("=" * 70)
    print(f"{'ID':<4} | {'Date':<19} | {'Title':<20} | {'Category':<15} | {'Amount ($)'}")
    print("-" * 70)
    
    if not expenses:
        print("                 No expenses recorded yet.                           ")
    else:
        for item in expenses:
            print(f"{item['id']:<4} | {item['date']:<19} | {item['title'][:20]:<20} | {item['category'][:15]:<15} | ${item['amount']:>8.2f}")
    
    print("-" * 70)
    print(f"Total Spent             : ${summary['total_spent']:.2f}")
    print(f"Monthly Budget Target   : ${summary['monthly_budget']:.2f}")
    print(f"Remaining Balance       : ${summary['remaining_budget']:.2f}")
    print(f"Budget Utilization      : {summary['budget_used_percentage']:.1f}%")
    
    print("\n--- Spending Breakdown by Category ---")
    for cat, spent in summary["category_breakdown"].items():
        bar_len = int(spent / 25)  # $25 per block
        bar = "#" * min(bar_len, 25)
        print(f"  {cat:<18}: ${spent:>7.2f} | {bar}")
    print("=" * 70 + "\n")

def run_automated_demo():
    """Demonstrates expense tracker functionality with mock records."""
    print("--- Running Personal Expense Tracker Demo ---")
    sample_expenses = [
        {"id": 1, "title": "Grocery Shopping", "amount": 124.50, "category": "Food & Dining", "date": "2026-11-01 10:15:00"},
        {"id": 2, "title": "Metro Commute Pass", "amount": 45.00, "category": "Transportation", "date": "2026-11-02 08:30:00"},
        {"id": 3, "title": "Electric Bill", "amount": 85.20, "category": "Utilities", "date": "2026-11-02 14:00:00"},
        {"id": 4, "title": "Python Course Book", "amount": 39.99, "category": "Education", "date": "2026-11-03 18:20:00"},
        {"id": 5, "title": "Cinema & Popcorn", "amount": 28.00, "category": "Entertainment", "date": "2026-11-03 21:00:00"},
    ]
    print_expense_report(sample_expenses, monthly_budget=500.0)

if __name__ == "__main__":
    run_automated_demo()
