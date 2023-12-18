import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append({"name": task_string, "status": "Incomplete"})
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', f"{task['name']} - {task['status']}")

def delete_task():
    try:
        selected_index = task_listbox.curselection()
        if selected_index:
            task_listbox.delete(selected_index)
            tasks.pop(selected_index[0])
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def mark_complete():
    try:
        selected_index = task_listbox.curselection()
        if selected_index:
            task = tasks[selected_index[0]]
            if task['status'] == 'Incomplete':
                task['status'] = 'Complete'
                list_update()
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Mark Complete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        task_listbox.delete(0, 'end')
        tasks.clear()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

if __name__ == "__main__":
    tasks = [
        {"name": "Task 1", "status": "Incomplete"},
        {"name": "Task 2", "status": "Incomplete"},
        {"name": "Task 3", "status": "Incomplete"},
    ]

    guiWindow = tk.Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("600x450+450+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#B0C4DE")

    header_frame = tk.Frame(guiWindow, bg="#B0C4DE")
    functions_frame = tk.Frame(guiWindow, bg="#B0C4DE")
    listbox_frame = tk.Frame(guiWindow, bg="#B0C4DE")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Harlow Solid Italic", "30"),
        background="#B0C4DE",
        foreground="#000000"
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Times new roman", "18", "bold"),
        background="#B0C4DE",
        foreground="#000000"
    )
    task_label.place(x=30, y=10)

    task_field = ttk.Entry(
        functions_frame,
        font=("Times new roman", "18"),
        width=18,
        background="#FFF8DC",
        foreground="#000000"
    )
    task_field.place(x=30, y=60)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=20,
        command=add_task
    )

    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=20,
        command=delete_task
    )

    mark_complete_button = ttk.Button(
        functions_frame,
        text="Mark Complete",
        width=20,
        command=mark_complete
    )

    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=20,
        command=close
    )

    add_button.place(x=75, y=150)
    del_button.place(x=75, y=200)
    mark_complete_button.place(x=75, y=250)
    exit_button.place(x=75, y=300)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=25,
        height=12,
        font=("Times new roman", "15"),
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#0000FF",
        selectforeground="#FFFFFF"
    )
    task_listbox.place(x=10, y=20)

    list_update()

    guiWindow.mainloop()
