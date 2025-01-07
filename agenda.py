def add_contact(contacts, name, phone, email, favorite):
    contact = {"name": name, "phone": phone, "email": email, "favorite": favorite}
    contacts.append(contact)
    print(f"Contact {name} was successfully added!")
    return

def view_registered_contacts(contacts):
    print("\nContact List")
    for index, contact in enumerate(contacts, start=1):
        favorite = "★" if contact["favorite"] == "Y" else " "
        name = contact["name"]
        phone = contact["phone"]
        email = contact["email"]
        print(f"{index}. [{favorite}] {name} - {phone} / {email}")
    return

def edit_contact(contacts, contact_index, new_name, new_phone, new_email):
    adjusted_contact_index = int(contact_index) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contacts):
        contacts[adjusted_contact_index]["name"] = new_name
        contacts[adjusted_contact_index]["phone"] = new_phone
        contacts[adjusted_contact_index]["email"] = new_email
        print(f"Contact {contact_index} updated to {new_name} - {new_phone} / {new_email}")
    else:
        print("Invalid contact index.")
    return

def toggle_favorite_status(contacts, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    if contacts[adjusted_contact_index]["favorite"] == "Y": 
        contacts[adjusted_contact_index]["favorite"] = "N"
    elif contacts[adjusted_contact_index]["favorite"] == "N":
        contacts[adjusted_contact_index]["favorite"] = "Y"
    else:
        print("Invalid contact index.")
    return

def view_favorite_contacts(contacts):
    print("\nFavorite Contact List")
    for index, contact in enumerate(contacts, start=1):
        if contact["favorite"] == "Y":
            name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            print(f"{index}. {name} - {phone} / {email}")
    return

def delete_contact(contacts, contact_index):
    adjusted_contact_index = int(contact_index) - 1
    if adjusted_contact_index >= 0 and adjusted_contact_index < len(contacts):
        del contacts[adjusted_contact_index]
        print(f"Contact {contact_index} was successfully deleted!")
    else:
        print("Invalid contact index.")
    return


contacts = []
while True:
    print("\nContact List")
    print("1. Add Contact")
    print("2. View Registered Contacts")
    print("3. Edit Contact")
    print("4. Mark/Unmark Contact as Favorite")
    print("5. View Favorite Contacts")
    print("6. Delete Contact")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name of the contact you want to add: ")
        phone = input("Enter the phone number of the contact you want to add: ")
        email = input("Enter the email of the contact you want to add: ")
        favorite = input("Add this contact to favorites? [Y/N] ")
        add_contact(contacts, name, phone, email, favorite)
    elif choice == "2":
        view_registered_contacts(contacts)
    elif choice == "3":
        view_registered_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to edit: ")
        new_name = input("Enter the new name: ")
        new_phone = input("Enter the new phone number: ")
        new_email = input("Enter the new email: ")
        edit_contact(contacts, contact_index, new_name, new_phone, new_email)
    elif choice == "4":
        view_registered_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to mark/unmark as favorite: ")
        toggle_favorite_status(contacts, contact_index)
    elif choice == "5":
        view_favorite_contacts(contacts)
    elif choice == "6":
        view_registered_contacts(contacts)
        contact_index = input("Enter the number of the contact you want to delete: ")
        delete_contact(contacts, contact_index)
        view_registered_contacts(contacts)
    elif choice == "7":
        break

print("Program finished")

