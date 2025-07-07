import sqlite3

def init_db():
    conn = sqlite3.connect('database/tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT,
            status TEXT DEFAULT 'Pending'
        )
    ''')
    conn.commit()
    conn.close()

def add_task(title, due_date):
    conn = sqlite3.connect('database/tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, due_date) VALUES (?, ?)", (title, due_date))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect('database/tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def mark_done(task_id):
    conn = sqlite3.connect('database/tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
