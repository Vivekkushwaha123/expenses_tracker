# Personal Expense Tracker with CSV
# Record expenses, save them to expenses.csv, filter them and see summaries.

import csv
import math
from datetime import datetime

FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]
CATEGORIES = ["Food", "Travel", "Study", "Bills", "Fun"]


# ---------- Storage helpers ----------

# Create expenses.csv with the header row if it does not exist yet
def ensure_file():
    try:
        open(FILE).close()
    except FileNotFoundError:
        with open(FILE, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, FIELDS).writeheader()


# Read every expense from the file and return a list of dictionaries
def load_expenses():
    try:
        with open(FILE, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


# Add one expense (a dictionary) to the end of the file
def save_expense(row):
    ensure_file()
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, FIELDS).writerow(row)


# ---------- Input helpers (validate at the moment we read) ----------

# Ask for a date in YYYY-MM-DD format until it is valid
def read_date(prompt):
    while True:
        text = input(prompt).strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD, for example 2026-10-04.")


# Ask for a month in YYYY-MM format until it is valid
def read_month(prompt):
    while True:
        text = input(prompt).strip()
        try:
            datetime.strptime(text, "%Y-%m")
            return text
        except ValueError:
            print("Invalid month. Use YYYY-MM, for example 2026-10.")


# Ask for a positive amount until it is valid
def read_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Please enter a number, for example 120.50.")
            continue
        if not math.isfinite(amount) or amount <= 0:
            print("The amount must be a number greater than zero.")
            continue
        return amount


# Show the category list and return the one the user picks
def choose_category():
    while True:
        print("\nCategories:")
        for number, name in enumerate(CATEGORIES, start=1):
            print(f"{number}) {name}")
        choice = input("Choose a category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print(f"Please pick a number from 1 to {len(CATEGORIES)}.")


# Ask for a description that is not empty
def read_description(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("The description cannot be empty.")


# ---------- Features ----------

# Menu option 1: ask for the details and save a new expense
def add_expense():
    print("\n--- Add expense ---")
    date = read_date("Date (YYYY-MM-DD): ")
    category = choose_category()
    description = read_description("Description: ")
    amount = read_amount("Amount: ")

    save_expense({
        "date": date,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}",
    })
    print("Expense saved!")


# Print a list of expenses in a tidy table with a total at the end
def print_table(rows):
    if not rows:
        print("No expenses found.")
        return

    print(f"\n{'Date':<12}{'Category':<10}{'Description':<24}{'Amount':>10}")
    print("-" * 56)
    for r in rows:
        print(f"{r['date']:<12}{r['category']:<10}{r['description'][:22]:<24}"
              f"{float(r['amount']):>10.2f}")
    print("-" * 56)
    total = sum(float(r["amount"]) for r in rows)
    print(f"{'Total':<46}{total:>10.2f}")


# Menu option 2: show every expense
def view_all():
    print("\n--- All expenses ---")
    print_table(load_expenses())


# Keep only the expenses of one category
def filter_by_category(rows, category):
    return [r for r in rows if r["category"] == category]


# Keep only the expenses of one month (first 7 characters of the date)
def filter_by_month(rows, month):
    return [r for r in rows if r["date"][:7] == month]


# Menu option 3: filter by category or by month
def filter_menu():
    print("\n--- Filter expenses ---")
    print("1) By category")
    print("2) By month")
    choice = input("Choose a filter: ").strip()
    rows = load_expenses()

    if choice == "1":
        category = choose_category()
        print_table(filter_by_category(rows, category))
    elif choice == "2":
        month = read_month("Month (YYYY-MM): ")
        print_table(filter_by_month(rows, month))
    else:
        print("Please pick 1 or 2.")


# Add up the spending of each category using a dictionary
def totals_by_category(rows):
    totals = {}
    for r in rows:
        totals[r["category"]] = totals.get(r["category"], 0) + float(r["amount"])
    return totals


# Menu option 4: totals per category, grand total and biggest expense
def show_summary():
    rows = load_expenses()
    print("\n--- Summary ---")
    if not rows:
        print("No expenses yet.")
        return

    totals = totals_by_category(rows)
    print(f"{'Category':<12}{'Total':>10}")
    print("-" * 22)
    for category, total in sorted(totals.items(), key=lambda item: item[1], reverse=True):
        print(f"{category:<12}{total:>10.2f}")
    print("-" * 22)
    print(f"{'Grand total':<12}{sum(totals.values()):>10.2f}")

    biggest = max(rows, key=lambda r: float(r["amount"]))
    print(f"\nBiggest expense: {biggest['description']} "
          f"({biggest['category']}, {biggest['date']}) - {float(biggest['amount']):.2f}")


# ---------- Main menu ----------

def main():
    ensure_file()
    while True:
        print("\n===== Expense Tracker =====")
        print("1) Add expense")
        print("2) View all")
        print("3) Filter")
        print("4) Summary")
        print("5) Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            filter_menu()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please pick a number from 1 to 5.")


if __name__ == "__main__":
    main()