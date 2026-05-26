#CHABIT

import tkinter as tk
from tkinter import messagebox
import json
import os

# WINDOW
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("750x600")
root.config(bg="#1E1E2F")
root.resizable(False, False)

# TITLE
title_label = tk.Label(
    root,
    text="Expense Tracker System",
    font=("Arial", 24, "bold"),
    bg="#1E1E2F",
    fg="white"
)

title_label.pack(pady=20)

# INPUT FRAME
frame = tk.Frame(
    root,
    bg="#2C2C3E",
    padx=20,
    pady=20
)

frame.pack(pady=10)

# Expense Name
label_name = tk.Label(
    frame,
    text="Expense Name:",
    bg="#2C2C3E",
    fg="white",
    font=("Arial", 12)
)

label_name.grid(row=0, column=0, pady=10)

entry_name = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12)
)

entry_name.grid(row=0, column=1, padx=10)

# Amount
label_amount = tk.Label(
    frame,
    text="Amount:",
    bg="#2C2C3E",
    fg="white",
    font=("Arial", 12)
)

label_amount.grid(row=1, column=0, pady=10)

entry_amount = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12)
)

entry_amount.grid(row=1, column=1)

# Category
label_category = tk.Label(
    frame,
    text="Category:",
    bg="#2C2C3E",
    fg="white",
    font=("Arial", 12)
)

label_category.grid(row=2, column=0, pady=10)

entry_category = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12)
)

entry_category.grid(row=2, column=1)

#ACHACOSO

# EXPENSE LIST
expense_list = []

# ADD EXPENSE FUNCTION
def add_expense():

    name = entry_name.get()
    amount = entry_amount.get()
    category = entry_category.get()

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expense_list.append(expense)

    listbox.insert(
        tk.END,
        f"{name} | ₱{amount} | {category}"
    )

# BUTTON FRAME
button_frame = tk.Frame(
    root,
    bg="#1E1E2F"
)

button_frame.pack(pady=10)

# ADD BUTTON
button_add = tk.Button(
    button_frame,
    text="Add Expense",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    command=add_expense
)

button_add.grid(row=0, column=0, padx=10)

#REGENCIA

# LISTBOX
listbox = tk.Listbox(
    root,
    width=80,
    height=15,
    font=("Arial", 11),
    bg="#F5F5F5"
)

listbox.pack(pady=10)

# TOTAL FUNCTION
def update_total():

    total = 0

    for expense in expense_list:
        total += float(expense["amount"])

    total_label.config(
        text=f"Total Expenses: ₱{total:.2f}"
    )

# TOTAL LABEL
total_label = tk.Label(
    root,
    text="Total Expenses: ₱0.00",
    font=("Arial", 16, "bold"),
    bg="#1E1E2F",
    fg="#FFD700"
)

total_label.pack(pady=10)

#OLANO

FILE_NAME = "expenses.json"

# SAVE FUNCTION
def save_expenses():

    with open(FILE_NAME, "w") as file:
        json.dump(expense_list, file, indent=4)

# LOAD FUNCTION
def load_expenses():

    global expense_list

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:

            expense_list = json.load(file)

            for expense in expense_list:

                listbox.insert(
                    tk.END,
                    f"{expense['name']} | ₱{expense['amount']} | {expense['category']}"
                )

# DELETE FUNCTION
def delete_expense():

    selected = listbox.curselection()

    if selected:

        index = selected[0]

        listbox.delete(index)

        expense_list.pop(index)

        save_expenses()

# DELETE BUTTON
button_delete = tk.Button(
    button_frame,
    text="Delete Expense",
    bg="#E53935",
    fg="white",
    font=("Arial", 12, "bold"),
    width=15,
    command=delete_expense
)

button_delete.grid(row=0, column=1, padx=10)
