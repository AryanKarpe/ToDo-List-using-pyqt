import tkinter as tk
from tkinter import ttk, messagebox

class TodoListApp:
    def __init__(abc, mainwindow):
        icon_path = 'C:\\Users\\ASUS\\Downloads\\icon.ico'

        abc.master = mainwindow
        abc.master.title("To-Do List")
        abc.master.iconbitmap(icon_path)
        
        abc.todo_listbox = tk.Listbox(mainwindow, selectmode=tk.SINGLE, height=15, width=40)
        abc.todo_listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        abc.task_entry = ttk.Entry(mainwindow, width=30, font=("San Francisco", 12))
        abc.task_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

        add_button = ttk.Button(mainwindow, text="Add Task", command=abc.add_task)
        add_button.grid(row=1, column=0, padx=5, pady=5)

        delete_button = ttk.Button(mainwindow, text="Delete Task", command=abc.delete_task)
        delete_button.grid(row=1, column=1, padx=5, pady=5)

        clear_button = ttk.Button(mainwindow, text="Clear All", command=abc.clear_all_tasks)
        clear_button.grid(row=1, column=2, pady=10)
        
        abc.task_entry.bind("<Return>", lambda event: abc.add_task())


    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_task_index = self.todo_listbox.curselection()
        if selected_task_index:
            self.todo_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")

    def clear_all_tasks(self):
        confirmed = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
        if confirmed:
            self.todo_listbox.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
