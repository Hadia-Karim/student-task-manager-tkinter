import tkinter as tk
from db import init_db
from dashboard import open_dashboard
from add_task import open_add_task
from task_list import open_task_list

def main():
    init_db()

    root = tk.Tk()
    root.title("Student Task Manager")
    root.geometry("400x300")

    tk.Label(root, text="📘 Student Task Manager", font=("Arial", 16, "bold")).pack(pady=15)

    tk.Button(root, text="Open Dashboard", width=30, command=open_dashboard).pack(pady=5)
    tk.Button(root, text="Add Task", width=30, command=open_add_task).pack(pady=5)
    tk.Button(root, text="View Tasks", width=30, command=open_task_list).pack(pady=5)

    tk.Label(root, text="© Team Hadia, Minahil", font=("Arial", 9)).pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
