# prompt: create a GUI based application using  python code for a to-do list application that helps users to manage and organize their task effficiently ,allowing user to create ,update and track their to-do list

import tkinter as tk
from tkinter import ttk, messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        # Task Listbox
        self.task_listbox = tk.Listbox(master, width=40)
        self.task_listbox.pack(pady=10)

        # Entry for new tasks
        self.new_task_entry = tk.Entry(master, width=30)
        self.new_task_entry.pack()

        # Buttons
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.pack(pady=5)

    def add_task(self):
        task = self.new_task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.new_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def edit_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]

            def save_edit():
                new_task = edit_entry.get()
                if new_task:
                    self.tasks[selected_index] = new_task
                    self.update_listbox()
                    edit_window.destroy()
                else:
                    messagebox.showwarning("Warning", "Please enter a task.")

            edit_window = tk.Toplevel(self.master)
            edit_window.title("Edit Task")
            edit_label = tk.Label(edit_window, text="Edit Task:")
            edit_label.pack()
            edit_entry = tk.Entry(edit_window, width=30)
            edit_entry.insert(0, task)
            edit_entry.pack()
            save_button = tk.Button(edit_window, text="Save", command=save_edit)
            save_button.pack(pady=5)

        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()