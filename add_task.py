import tkinter as tk
from tkinter import messagebox
from db import add_task

def open_add_task():
    window = tk.Toplevel()
    window.title("Add Task")

    tk.Label(window, text="Task Title:").pack()
    title_entry = tk.Entry(window, width=40)
    title_entry.pack()

    tk.Label(window, text="Due Date (YYYY-MM-DD):").pack()
    date_entry = tk.Entry(window, width=40)
    date_entry.pack()

    def save():
        title = title_entry.get()
        due_date = date_entry.get()
        if title.strip() == "":
            messagebox.showwarning("Warning", "Task title is required.")
        else:
            add_task(title, due_date)
            messagebox.showinfo("Success", "Task added successfully!")
            window.destroy()

    tk.Button(window, text="Add Task", command=save).pack(pady=10)
