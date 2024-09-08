import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        self.contacts = []

        # Add Contact Button
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        # View Contacts Button
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        # Search Contact Button
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        # Update Contact Button
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        # Delete Contact Button
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        # Listbox to display contacts
        self.contact_listbox = tk.Listbox(root, width=50, height=15)
        self.contact_listbox.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        phone = simpledialog.askstring("Add Contact", "Enter phone number:")
        email = simpledialog.askstring("Add Contact", "Enter email:")
        address = simpledialog.askstring("Add Contact", "Enter address:")
        
        if name and phone:
            self.contacts.append({
                "name": name, 
                "phone": phone, 
                "email": email if email else "N/A", 
                "address": address if address else "N/A"
            })
            self.update_contact_listbox()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def view_contacts(self):
        self.update_contact_listbox()

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number to search:")
        if search_term:
            results = [contact for contact in self.contacts if search_term in contact["name"] or search_term in contact["phone"]]
            if results:
                self.contact_listbox.delete(0, tk.END)
                for contact in results:
                    self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
            else:
                messagebox.showinfo("No Results", "No contacts found matching the search term.")
        else:
            messagebox.showerror("Error", "Please enter a name or phone number to search.")

    def update_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index:
            index = selected_contact_index[0]
            contact = self.contacts[index]

            new_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact["name"])
            new_phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact["phone"])
            new_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact["email"])
            new_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact["address"])

            if new_name and new_phone:
                self.contacts[index] = {
                    "name": new_name,
                    "phone": new_phone,
                    "email": new_email if new_email else "N/A",
                    "address": new_address if new_address else "N/A"
                }
                self.update_contact_listbox()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Name and phone number are required.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_contact_index = self.contact_listbox.curselection()
        if selected_contact_index:
            index = selected_contact_index[0]
            confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
            if confirm:
                del self.contacts[index]
                self.update_contact_listbox()
                messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
