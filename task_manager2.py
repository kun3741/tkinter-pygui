import tkinter as tk
from tkinter import messagebox
import json

def save_tasks():
    all_tasks = listbox.get(0, tk.END)
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(all_tasks, file)

def load_tasks():
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def add_task():
    task = entry.get().strip()
    
    if task == "":
        messagebox.showwarning("Warning", "You cannot add an empty task!")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index[0])
        save_tasks()

def clear_all():
    listbox.delete(0, tk.END)
    save_tasks()

window = tk.Tk()
window.title("Task Manager")
window.geometry("400x450")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

add_button = tk.Button(window, text="Add task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete selected", command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(window, text="Clear all", command=clear_all)
clear_button.pack(pady=5)

load_tasks()

window.mainloop()
