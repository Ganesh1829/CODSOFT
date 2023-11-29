import tkinter as tk
from tkinter import messagebox

contacts = {}


def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name.strip() == '' or phone.strip() == '':
        messagebox.showwarning("Warning", "Please enter name and phone number.")
    else:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
        clear_entries()


def view_contacts():
    contact_list.delete(0, tk.END)
    if not contacts:
        contact_list.insert(tk.END, "Contact book is empty.")
    else:
        for name, details in contacts.items():
            contact_list.insert(tk.END, f"Name: {name}")
            contact_list.insert(tk.END, f"Phone: {details['Phone']}")
            contact_list.insert(tk.END, f"Email: {details['Email']}")
            contact_list.insert(tk.END, f"Address: {details['Address']}")
            contact_list.insert(tk.END, "-" * 20)


def delete_contact():
    selected_contact = contact_list.curselection()
    if not selected_contact:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
    else:
        index = selected_contact[0]
        name_to_delete = contact_list.get(index).split(": ")[1]

        if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete '{name_to_delete}'?"):
            del contacts[name_to_delete]
            messagebox.showinfo("Success", f"Contact '{name_to_delete}' deleted successfully.")
            view_contacts()


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)


def main():
    root = tk.Tk()
    root.title("Contact Book")

    global entry_name, entry_phone, entry_email, entry_address, contact_list

    label_name = tk.Label(root, text="Name:")
    label_name.grid(row=0, column=0, padx=5, pady=5)
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    label_phone = tk.Label(root, text="Phone:")
    label_phone.grid(row=1, column=0, padx=5, pady=5)
    entry_phone = tk.Entry(root)
    entry_phone.grid(row=1, column=1, padx=5, pady=5)

    label_email = tk.Label(root, text="Email:")
    label_email.grid(row=2, column=0, padx=5, pady=5)
    entry_email = tk.Entry(root)
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    label_address = tk.Label(root, text="Address:")
    label_address.grid(row=3, column=0, padx=5, pady=5)
    entry_address = tk.Entry(root)
    entry_address.grid(row=3, column=1, padx=5, pady=5)

    button_add = tk.Button(root, text="Add Contact", command=add_contact)
    button_add.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    button_view = tk.Button(root, text="View Contacts", command=view_contacts)
    button_view.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    contact_list = tk.Listbox(root, width=40)
    contact_list.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    button_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
    button_delete.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

    button_clear = tk.Button(root, text="Clear Entries", command=clear_entries)
    button_clear.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
