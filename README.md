#  Student Task Manager – Tkinter GUI App

This is a collaborative **Tkinter-based Python GUI application** built as part of our **Open Source Software Development (OSSD)** final term project. The app allows students to manage their academic tasks with features like adding tasks, viewing tasks, and marking them as completed. The project also incorporates GitHub-based version control to demonstrate collaborative open-source development workflows.

---

##  Feature Summary

- Add new tasks with a title and due date.
- View all tasks in a structured list format.
- Mark tasks as "Completed".
- Task data saved persistently using SQLite.
- Modular GUI with 3 separate windows (screens).
- Clean layout using `pack()` and `grid()`.

---

##  Tools and Technologies Used

| Tool / Tech      | Purpose                     |
|------------------|-----------------------------|
| Python           | Core programming language   |
| Tkinter          | GUI framework               |
| SQLite           | Database (local persistence)|
| Git              | Version control             |
| GitHub (Public)  | Hosting repository & collab |

---

##  Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Hadia-Karim/student-task-manager-tkinter.git
   cd student-task-manager-tkinter
   ```

2. **Run the App**
   ```bash
   python main.py
   ```

> No external libraries are required. Python 3.x comes with Tkinter and SQLite pre-installed.

---

##  Screenshots

> *(Add screenshots or screen recordings of: Dashboard, Add Task window, Task List screen)*

---

##  Contribution Credits

| Name     | Role                        | Branch Name         |
|----------|-----------------------------|---------------------|
| Hadia *(Leader)* | Dashboard GUI, main launcher, README, reports | `dashboard-hadia` |
| Minahil           | Add Task screen, Task List screen, database | `tasklist-minahil` |

---

##  GitHub Collaboration (Workflow)

- Each member worked on their **feature branch**
- Created and resolved GitHub **Issues**:
  - e.g., `Add Task Screen`, `Fix status bug`
- Opened Pull Requests (PRs) with messages like:
  ```
  Fixes #2 – Implemented Task Viewer screen
  ```
- Participated in code reviews and testing

---

##  Links to Major PRs and Issues

| Issue/PR            | Link Example                |
|---------------------|-----------------------------|
| Add Task Screen     | `Fixes #2` via [PR #3](https://github.com/Hadia-Karim/student-task-manager-tkinter/pulls) |
| Task List View      | `Fixes #4` via [PR #5](https://github.com/Hadia-Karim/student-task-manager-tkinter/pulls) |
| Mark as Done Bugfix | `Fixes #6` via [PR #7](https://github.com/Hadia-Karim/student-task-manager-tkinter/pulls) |

*(Replace the links after pushing to GitHub)*

---

##  Backend / Database Explanation

The app uses **SQLite** for saving all tasks persistently in a local database file:

- File: `tasks.db` (auto-generated inside `/database`)
- Table: `tasks`
- Columns: `id`, `title`, `due_date`, `status`
- Operations:
  - Insert task (`add_task()`)
  - Retrieve all tasks (`get_all_tasks()`)
  - Update status (`mark_done()`)

---

##  License

This project is submitted for academic purposes under the Final Term OSSD (Open Source Software Development) course at **University of Management and Technology**.
