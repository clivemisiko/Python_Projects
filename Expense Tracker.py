import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

# File to store expense data
DATA_FILE = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add an expense
def add_expense():
    date = date_entry.get()
    category = category_combobox.get()
    amount = amount_entry.get()

    if not date or not category or not amount:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number.")
        return

    expenses.append({"date": date, "category": category, "amount": amount})
    save_expenses(expenses)
    messagebox.showinfo("Success", "Expense added successfully.")
    clear_entries()
    update_report()

# Clear input fields
def clear_entries():
    date_entry.delete(0, tk.END)
    category_combobox.set("")
    amount_entry.delete(0, tk.END)

# Generate and display a summarized report
def update_report():
    report_text.delete(1.0, tk.END)

    # Group expenses by date or category
    report_type = report_type_combobox.get()
    if report_type == "By Date":
        grouped_expenses = {}
        for expense in expenses:
            date = expense["date"]
            if date not in grouped_expenses:
                grouped_expenses[date] = []
            grouped_expenses[date].append(expense)
    else:
        grouped_expenses = {}
        for expense in expenses:
            category = expense["category"]
            if category not in grouped_expenses:
                grouped_expenses[category] = []
            grouped_expenses[category].append(expense)

    # Display the report
    for key, items in grouped_expenses.items():
        report_text.insert(tk.END, f"{key}:\n")
        total = 0
        for item in items:
            report_text.insert(tk.END, f"  - {item['category']}: ksh{item['amount']:.2f}\n")
            total += item["amount"]
        report_text.insert(tk.END, f"  Total: ksh{total:.2f}\n\n")

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("600x500")

# Load existing expenses
expenses = load_expenses()

# Input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

date_label = tk.Label(input_frame, text="Date (YYYY-MM-DD):", font=("Arial", 12))
date_label.grid(row=0, column=0, padx=5, pady=5)

date_entry = tk.Entry(input_frame, font=("Arial", 12))
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(input_frame, text="Category:", font=("Arial", 12))
category_label.grid(row=1, column=0, padx=5, pady=5)

category_combobox = ttk.Combobox(input_frame, values=["Food", "Bills", "Transport", "Entertainment", "Other"], font=("Arial", 12))
category_combobox.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(input_frame, text="Amount (ksh):", font=("Arial", 12))
amount_label.grid(row=2, column=0, padx=5, pady=5)

amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(input_frame, text="Add Expense", font=("Arial", 12), command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Report type selection
report_frame = tk.Frame(root)
report_frame.pack(pady=10)

report_type_label = tk.Label(report_frame, text="Report Type:", font=("Arial", 12))
report_type_label.grid(row=0, column=0, padx=5, pady=5)

report_type_combobox = ttk.Combobox(report_frame, values=["By Date", "By Category"], font=("Arial", 12))
report_type_combobox.grid(row=0, column=1, padx=5, pady=5)
report_type_combobox.current(0)

update_button = tk.Button(report_frame, text="Update Report", font=("Arial", 12), command=update_report)
update_button.grid(row=0, column=2, padx=5, pady=5)

# Report display
report_text = tk.Text(root, font=("Arial", 12), wrap=tk.WORD)
report_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Initial report update
update_report()

# Run the application
root.mainloop()