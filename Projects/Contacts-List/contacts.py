# CONTACTS LIST IN YOUR PHONE

print("CONTACTS LIST IN OUR PHONE")

contacts = {}


def menu():
    print("""
    1. Add Contact
    2. View Contacts
    3. Search Contact
    4. Delete Contact
    5. Edit Contact Number
    6. Edit Contact Name
    7. Exit
    """)


def add_contact(name, phone_number):
    if name in contacts:
        print("This contact already exists.")
        print(f"{name}: {contacts[name]}")
    else:
        contacts[name] = phone_number
        print(f"{name} added successfully.")


def view_contacts():
    if not contacts:
        print("Contact list is empty.")
        return

    print("\nYour Phone Contacts List:")
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")


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

    print(f"After : {new_name}: {contacts[new_name]}")


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

        delete_contact(name)

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
        print("Goodbye.")
        break

    else:
        print("Please enter a valid choice.")