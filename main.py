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
