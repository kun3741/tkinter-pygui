import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index[0])

window = tk.Tk()
window.title("Task Manager")
window.geometry("400x400")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

add_button = tk.Button(window, text="Add task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete selected", command=delete_task)
delete_button.pack(pady=5)

window.mainloop()
