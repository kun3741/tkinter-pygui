import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import json

tasks_data = [] 
PRIORITY_WEIGHT = {"High": 1, "Medium": 2, "Low": 3}

def update_ui():
    listbox.delete(0, tk.END)
    tasks_data.sort(key=lambda x: PRIORITY_WEIGHT.get(x["priority"], 3))
    for task in tasks_data:
        listbox.insert(tk.END, f"[{task['priority']}] {task['task']}")

def add_task():
    task_text = entry.get().strip()
    priority = priority_combobox.get()
    
    if task_text == "":
        messagebox.showwarning("Warning", "You cannot add an empty task!")
    else:
        tasks_data.append({"task": task_text, "priority": priority})
        entry.delete(0, tk.END)
        update_ui()

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        del tasks_data[index]
        update_ui()

def clear_all():
    tasks_data.clear()
    update_ui()

def save_tasks_as():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        title="Save tasks as"
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(tasks_data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def open_tasks():
    file_path = filedialog.askopenfilename(
        defaultextension=".json",
        filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        title="Open tasks"
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                global tasks_data
                tasks_data = json.load(file)
                update_ui()
        except Exception as e:
            messagebox.showerror("Error", f"Could not load file: {e}")

def show_about():
    messagebox.showinfo("About", "Task Manager\nCreated by: kun3741\n\nThis program helps you manage your tasks with their priorities.")

window = tk.Tk()
window.title("Task Manager")
window.geometry("450x450")
menubar = tk.Menu(window)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open...", command=open_tasks)
file_menu.add_command(label="Save As...", command=save_tasks_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menubar.add_cascade(label="Help", menu=help_menu)

window.config(menu=menubar)

window.columnconfigure(1, weight=1)

tk.Label(window, text="Task:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=1, padx=10, pady=10, sticky="we")

tk.Label(window, text="Priority:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
priority_combobox = ttk.Combobox(window, values=["High", "Medium", "Low"], state="readonly")
priority_combobox.current(1)
priority_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="we")

add_button = tk.Button(window, text="Add task", command=add_task)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

listbox = tk.Listbox(window, width=50, height=10)
listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

delete_button = tk.Button(window, text="Delete selected", command=delete_task)
delete_button.grid(row=4, column=0, columnspan=2, pady=5)

clear_button = tk.Button(window, text="Clear all", command=clear_all)
clear_button.grid(row=5, column=0, columnspan=2, pady=5)

window.mainloop()
