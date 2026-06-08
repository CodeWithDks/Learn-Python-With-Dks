# CONTACTS LIST IN YOUR PHONE

import json

print("CONTACTS LIST IN OUR PHONE")

contacts = {}


def load_contacts():
    global contacts

    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

    except FileNotFoundError:
        contacts = {}

    except json.JSONDecodeError:
        print("Contacts file is corrupted. Starting with an empty contact list.")
        contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def menu():
    print("""
    1. Add Contact
    2. View Contacts
    3. Search Contact
    4. Delete Contact
    5. Edit Contact Number
    6. Edit Contact Name
    7. All Contact List.
    8. Exit
    """)


def add_contact(name, phone_number):
    if name in contacts:
        print("This contact already exists.")
        print(f"{name}: {contacts[name]}")
    else:
        contacts[name] = phone_number
        save_contacts()
        print(f"{name} added successfully.")


def view_contacts():
    print(f"\nTotal Contacts: {len(contacts)}")

    if not contacts:
        print("Contact list is empty.")
        return

    print("\nYour Phone Contacts List:")

    for name in sorted(contacts):
        print(f"{name}: {contacts[name]}")


def search_contact(name):
    if not contacts:
        print("Contact list is empty.")
        return

    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact(name):
    if not contacts:
        print("Contact list is empty. Nothing to delete.")
        return

    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")


def edit_contact_number(name, new_phone_number):
    if not contacts:
        print("Contact list is empty.")
        return

    if name in contacts:
        print(f"Before: {name}: {contacts[name]}")
        contacts[name] = new_phone_number
        save_contacts()
        print(f"After : {name}: {contacts[name]}")
    else:
        print("Contact not found.")


def edit_contact_name(old_name, new_name):
    if not contacts:
        print("Contact list is empty.")
        return

    if old_name not in contacts:
        print("Contact not found.")
        return

    if new_name in contacts:
        print("A contact with this name already exists.")
        return

    print(f"Before: {old_name}: {contacts[old_name]}")

    contacts[new_name] = contacts.pop(old_name)
    save_contacts()

    print(f"After : {new_name}: {contacts[new_name]}")


def contact_count():
    if not contacts:
        print("Contact list is empty.")
    else:
        print(f"Total Contacts: {len(contacts)}")


load_contacts()


while True:
    menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip().title()

        if not name:
            print("Name can't be empty.")
            continue

        phone_number = input("Enter contact number: ").strip()

        if not phone_number.isdigit():
            print("Phone number must contain only digits.")
            continue

        if len(phone_number) != 10:
            print("Phone number must be exactly 10 digits.")
            continue

        if phone_number in contacts.values():
            print("Phone number already exists.")
            continue

        add_contact(name, phone_number)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        name = input("Enter contact name to search: ").strip().title()

        if not name:
            print("Name can't be empty.")
            continue

        search_contact(name)

    elif choice == "4":
        name = input("Enter contact name to delete: ").strip().title()

        if not name:
            print("Name can't be empty.")
            continue

        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            delete_contact(name)
        else:
            print("Delete operation cancelled.")


    elif choice == "5":
        name = input("Enter contact name: ").strip().title()

        if not name:
            print("Name can't be empty.")
            continue

        new_phone_number = input("Enter new phone number: ").strip()

        if not new_phone_number.isdigit():
            print("Phone number must contain only digits.")
            continue

        if len(new_phone_number) != 10:
            print("Phone number must be exactly 10 digits.")
            continue

        if (
            new_phone_number in contacts.values()
            and contacts.get(name) != new_phone_number
        ):
            print("Phone number already exists.")
            continue

        edit_contact_number(name, new_phone_number)

    elif choice == "6":
        old_name = input("Enter old name: ").strip().title()

        if not old_name:
            print("Name can't be empty.")
            continue

        new_name = input("Enter new name: ").strip().title()

        if not new_name:
            print("Name can't be empty.")
            continue

        edit_contact_name(old_name, new_name)


    elif choice == "7":
        contact_count()

        
    elif choice == "8":
        print("Goodbye.")
        break

    else:
        print("Please enter a valid choice.")