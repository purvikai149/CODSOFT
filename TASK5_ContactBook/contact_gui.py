import tkinter as tk
from tkinter import messagebox
#Data Storage
contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required.")
        return

    #for duplicate name
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            messagebox.showerror("Error", "Contact with this name already exists.")
            return

    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })

    refresh_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact added successfully!")

def refresh_contacts():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} | {contact['phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

def load_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact.")
        return

    index = selected[0]
    contact = contacts[index]

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

    name_entry.insert(0, contact['name'])
    phone_entry.insert(0, contact['phone'])
    email_entry.insert(0, contact['email'])
    address_entry.insert(0, contact['address'])

def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to update.")
        return

    index = selected[0]

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if not name or not phone:
        messagebox.showerror("Error", "Name and Phone are required.")
        return

    contacts[index] = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    refresh_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact updated successfully!")

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Please select a contact to delete.")
        return

    index = selected[0]
    contacts.pop(index)
    refresh_contacts()
    clear_fields()
    messagebox.showinfo("Success", "Contact deleted successfully!")

def search_contact():
    query = search_entry.get().strip().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} | {contact['phone']}")
    if contact_list.size() == 0:
        messagebox.showinfo("Search", "No contacts found.")

root = tk.Tk()
root.title("Contact Management System")

#Frames
left_frame = tk.Frame(root, padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="n")

right_frame = tk.Frame(root, padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="n")

#Input fields
tk.Label(left_frame, text="Name").grid(row=0, column=0, sticky="w")
tk.Label(left_frame, text="Phone").grid(row=1, column=0, sticky="w")
tk.Label(left_frame, text="Email").grid(row=2, column=0, sticky="w")
tk.Label(left_frame, text="Address").grid(row=3, column=0, sticky="w")

name_entry = tk.Entry(left_frame, width=30)
phone_entry = tk.Entry(left_frame, width=30)
email_entry = tk.Entry(left_frame, width=30)
address_entry = tk.Entry(left_frame, width=30)

name_entry.grid(row=0, column=1, pady=2)
phone_entry.grid(row=1, column=1, pady=2)
email_entry.grid(row=2, column=1, pady=2)
address_entry.grid(row=3, column=1, pady=2)

#Buttons
tk.Button(left_frame, text="Add Contact", width=15, command=add_contact).grid(row=4, column=0, pady=5)
tk.Button(left_frame, text="Load Selected", width=15, command=load_contact).grid(row=4, column=1, pady=5)
tk.Button(left_frame, text="Update Contact", width=15, command=update_contact).grid(row=5, column=0, pady=5)
tk.Button(left_frame, text="Delete Contact", width=15, command=delete_contact).grid(row=5, column=1, pady=5)
tk.Button(left_frame, text="Clear Fields", width=32, command=clear_fields).grid(row=6, column=0, columnspan=2, pady=5)

#Search bar
tk.Label(left_frame, text="Search by Name or Phone:").grid(row=7, column=0, sticky="w")
search_entry = tk.Entry(left_frame, width=20)
search_entry.grid(row=7, column=1, pady=2, sticky="w")
tk.Button(left_frame, text="Search", width=32, command=search_contact).grid(row=8, column=0, columnspan=2, pady=5)

#Contact List
tk.Label(right_frame, text="Saved Contacts").pack(anchor="w")
contact_list = tk.Listbox(right_frame, width=50, height=20)
contact_list.pack()

root.mainloop()
