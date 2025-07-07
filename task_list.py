import tkinter as tk
from tkinter import messagebox
from db import get_all_tasks, mark_done

def open_task_list():
    window = tk.Toplevel()
    window.title("Task List")

    tasks = get_all_tasks()

    for task in tasks:
        frame = tk.Frame(window, borderwidth=1, relief="solid", pady=5)
        frame.pack(fill="x", padx=10, pady=5)

        info = f"ID: {task[0]} | Title: {task[1]} | Due: {task[2]} | Status: {task[3]}"
        tk.Label(frame, text=info).pack()

        if task[3] == "Pending":
            def mark_done_closure(tid=task[0]):
                mark_done(tid)
                messagebox.showinfo("Updated", f"Task {tid} marked as done.")
                window.destroy()
                open_task_list()

            tk.Button(frame, text="Mark as Done", command=mark_done_closure).pack()
