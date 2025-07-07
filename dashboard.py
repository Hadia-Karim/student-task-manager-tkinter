import tkinter as tk
from tkinter import Label

def open_dashboard():
    window = tk.Toplevel()
    window.title("Dashboard")

    Label(window, text="🎓 Student Task Manager", font=("Arial", 16, "bold")).pack(pady=10)
    Label(window, text="Manage your assignments and deadlines easily!", font=("Arial", 12)).pack(pady=5)
