import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        label_status.config(text="Please enter a task!", fg="red")

def remove_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        label_status.config(text="", fg="black")
    except IndexError:
        label_status.config(text="No task selected.", fg="red")

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

label = tk.Label(frame, text="Enter Task:")
label.grid(row=0, column=0)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1)

add_button = tk.Button(frame, text="Add Task", width=15, command=add_task)
add_button.grid(row=0, column=2, padx=5)

remove_button = tk.Button(frame, text="Remove Task", width=15, command=remove_task)
remove_button.grid(row=1, column=2, pady=5)

listbox = tk.Listbox(frame, width=40, height=10)
listbox.grid(row=1, columnspan=2, pady=10)

label_status = tk.Label(frame, text="", fg="black")
label_status.grid(row=2, columnspan=3)

root.mainloop()
