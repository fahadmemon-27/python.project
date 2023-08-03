import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x800")
font = ("Arial", 20)
listbox = tk.Listbox(root, font=font)


def fetchContacts():
    data = list()
    with open('contacts.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            try:
                name, number = line.split(',')
                data.append({'name': name, 'number': number})
            except ValueError:
                pass
    return data


contacts = fetchContacts()


def updateData():
    listbox.delete(0, "end")
    for contact in contacts:
        name = contact['name']
        number = contact['number']
        listbox.insert(contacts.index(contact), f'{name}, {number}')


updateData()


def save_contact():
    name = entry_name.get()
    phone = entry_phone.get()

    if name and phone:
        contacts.append({'name': name, 'number': phone})
        updateData()
    else:
        messagebox.showerror(
            "Error", "Please enter both name and phone number.")


def delete_contact():
    """
    this funtion deletes the selected contact during runtime and not in txt file
    """
    try:
        selectedContact = listbox.curselection()[0]
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete")
        return

    contacts.pop(selectedContact)
    updateData()
    messagebox.showinfo("Success", "Contact deleted successfully.")


def update_contact():
    name = entry_name.get()
    phone = entry_phone.get()

    try:
        selectedContact = listbox.curselection()[0]
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to update...")
        return

    if name and phone:
        contacts[selectedContact]['name'] = name
        contacts[selectedContact]['number'] = phone
        updateData()
        messagebox.showinfo("Success", "Contact updated successfully.")

    else:
        messagebox.showerror(
            "Error", "Please enter both name and phone number to update the contact.")
        
        

def saveChangesOnExit():
    with open('contacts.txt', 'w') as file:
        for contact in contacts:
            name = contact['name']
            number = contact['number']
            file.write(f'{name}, {number}\n')
    
    root.destroy()

label_name = tk.Label(root, text="Name:", font=font)
label_name.pack()

entry_name = tk.Entry(root, width=18, font=font)
entry_name.pack()

label_phone = tk.Label(root, text="Phone:", font=font)
label_phone.pack()

entry_phone = tk.Entry(root, width=18, font=font)
entry_phone.pack()

button_save = tk.Button(root, text="Save Contact", command=save_contact, font=font, bg="light green")
button_save.pack(pady=12)

button_update = tk.Button(root, text="Update Contact", command=update_contact, font=font, bg="light blue")
button_update.pack(pady=12)

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact, font=font, bg='orange')
button_delete.pack(pady=12)
listbox.pack()

root.protocol('WM_DELETE_WINDOW', saveChangesOnExit)
root.mainloop()