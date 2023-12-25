contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("Contact List:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['Name']} | Phone: {contact['Phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = []
    
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            found_contacts.append(contact)
    
    if found_contacts:
        print("Search Results:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']} | Phone: {contact['Phone']} | Email: {contact['Email']} | Address: {contact['Address']}")
    else:
        print("No matching contacts found.")

def update_contact():
    search_term = input("Enter name or phone number of contact to update: ")
    found_contact = None
    
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            found_contact = contact
            break
    
    if found_contact:
        print(f"Contact found: Name: {found_contact['Name']} | Phone: {found_contact['Phone']}")
        choice = input("What do you want to update? (Name/Phone/Email/Address): ").lower()
        
        if choice == 'name':
            new_name = input("Enter new name: ")
            found_contact['Name'] = new_name
        elif choice == 'phone':
            new_phone = input("Enter new phone number: ")
            found_contact['Phone'] = new_phone
        elif choice == 'email':
            new_email = input("Enter new email address: ")
            found_contact['Email'] = new_email
        elif choice == 'address':
            new_address = input("Enter new address: ")
            found_contact['Address'] = new_address
        else:
            print("Invalid choice!")
    else:
        print("Contact not found.")

def delete_contact():
    search_term = input("Enter name or phone number of contact to delete: ")
    found_contact = None
    
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']:
            found_contact = contact
            break
    
    if found_contact:
        contacts.remove(found_contact)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
