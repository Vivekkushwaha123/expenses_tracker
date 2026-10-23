# Personal Expense Tracker with CSV

A beginner-friendly command-line program written in Python. It records daily expenses by category, saves them to a CSV file so they are still there after you restart, and shows filters and summaries.

## Features

- **Add** an expense with date, category, description and amount
- **View all** expenses in a tidy table with a total
- **Filter** by category or by month
- **Summary** with total per category, grand total and the biggest single expense
- Data is saved in `expenses.csv` and reloaded every time the program starts
- `expenses.csv` is created automatically (with the header row) if it is missing
- Input is validated: dates must be `YYYY-MM-DD`, amounts must be numbers greater than zero, and the description cannot be empty

## Categories

Food, Travel, Study, Bills, Fun (you can change the `CATEGORIES` list at the top of the code).

## How to run

1. Install Python 3.10 or newer (no extra packages needed; it uses the built-in `csv` and `datetime` modules).
2. Download or clone this repository.
3. Open a terminal in the folder and run:

```
python expense_tracker.py
```

## Menu

```
1) Add expense
2) View all
3) Filter
4) Summary
5) Quit
```

## Example of the CSV file

All data in this file is made up.

```
date,category,description,amount
2026-09-03,Food,Lunch at canteen,120.50
2026-09-05,Travel,Bus pass,450.00
2026-09-09,Study,Python notebook,85.00
2026-09-24,Food,"Groceries, vegetables",340.75
2026-10-01,Bills,Internet bill,599.00
2026-10-10,Study,Online course fee,999.00
```

## Example summary

```
Category         Total
----------------------
Study          1084.00
Food           1011.75
Bills           898.00
Travel          510.00
Fun             430.00
----------------------
Grand total    3933.75

Biggest expense: Online course fee (Study, 2026-10-10) - 999.00
```

## A problem I fixed

Write one real problem you faced here, for example: "Descriptions with a comma (like Groceries, vegetables) could break the file, so I used the csv module, which puts quotes around them automatically."

## What I learned

- Reading and writing CSV files with `csv.DictReader` and `csv.DictWriter`
- Validating dates with `datetime.strptime` and amounts with `float()`
- Grouping and totalling data with a dictionary
- Building a simple menu program with functions

## Author

Vivek Kushwaha