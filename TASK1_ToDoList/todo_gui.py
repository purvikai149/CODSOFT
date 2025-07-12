# Simple GUI To-Do List App using Tkinter
# Author:Purvika Thombare

import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            for line in f:
                tasks.append(line.strip())
    return tasks

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Update listbox with current tasks
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Add a new task
def add_task():
    task = entry.get().strip()
    if task != "":
        tasks.append(task)
        update_listbox()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Mark task as completed
def mark_complete():
    try:
        index = listbox.curselection()[0]
        task = tasks[index]
        if not task.endswith("(Done)"):
            tasks[index] = task + " (Done)"
            update_listbox()
            save_tasks()
        else:
            messagebox.showinfo("Info", "Task is already marked complete.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task!")

# Main GUI window
root = tk.Tk()
root.title("My To-Do List")

tasks = load_tasks()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

update_listbox()

entry = tk.Entry(frame, width=50)
entry.pack(pady=5)

add_btn = tk.Button(frame, text="Add Task", width=48, command=add_task)
add_btn.pack(pady=2)

mark_btn = tk.Button(frame, text="Mark as Complete", width=48, command=mark_complete)
mark_btn.pack(pady=2)

del_btn = tk.Button(frame, text="Delete Task", width=48, command=delete_task)
del_btn.pack(pady=2)

root.mainloop()
