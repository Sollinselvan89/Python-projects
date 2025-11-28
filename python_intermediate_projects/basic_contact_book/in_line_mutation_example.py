import json


def load_contact() -> list[dict[str, str]]:
    """
    Load contacts from 'contacts.json'.

    If the file does not exist, create an empty file and return an empty list.
    Assigns incremental IDs to each contact after loading.

    Returns:
        list[dict[str, str]]: List of contacts with assigned IDs.
    """
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            count = 0
            for contact in contacts:
                count += 1
                contact["id"] = count
            return contacts

    except FileNotFoundError:
        print("json file not found. Created an empty json file")
        with open("contacts.json", "w") as file:
            json.dump([], file, indent=4)
        return []


def get_user_input() -> str:
    """
    Display menu options and return the user's selection.

    Returns:
        str: The user's choice (1–4 or 'q').
    """
    print("What do you want to do with the contact list?")
    print("1 -> Create new contact")
    print("2 -> View the contact book")
    print("3 -> Update a contact")
    print("4 -> Delete a contact")
    print("q -> Quit")

    while True:
        user_choice = input("Enter your choice 1–4 or q: ").strip().lower()
        if user_choice in ["1", "2", "3", "4", "q"]:
            return user_choice
        print("Invalid option. Try again.")


def select_contact_id(contacts) -> int:
    """
    Prompt the user to select a contact ID.

    Args:
        contacts (list): List of contacts.

    Returns:
        int: Selected contact ID.
    """
    while True:
        cid = input("Select the contact ID: ").strip()
        if not cid:
            print("Field cannot be empty")
            continue
        try:
            cid = int(cid)
            if cid in range(1, len(contacts) + 1):
                return cid
            print("ID not in range.")
        except ValueError:
            print("Enter numbers only.")


def validate_name() -> str:
    """
    Validate and return a proper contact name.

    Returns:
        str: Valid name in title case.
    """
    while True:
        name = input("Enter name: ").strip().lower()
        if not name:
            print("Name cannot be empty")
            continue
        if any(ch.isdigit() for ch in name):
            print("Name cannot contain digits.")
            continue
        return name.title()


def validate_phone_num() -> int:
    """
    Validate and return a contact phone number.

    Returns:
        int: Valid phone number between 7–15 digits.
    """
    while True:
        num = input("Enter phone number: ").strip()
        if not num:
            print("Phone number cannot be empty")
            continue
        if not 7 <= len(num) <= 15:
            print("Phone must be 7–15 digits long.")
            continue
        if not num.isdigit():
            print("Digits only.")
            continue
        return int(num)


def validate_email() -> str:
    """
    Validate and return a contact email.

    Returns:
        str: A valid email containing '@' and '.'.
    """
    while True:
        email = input("Enter email: ").strip().lower()
        if not email:
            print("Email cannot be empty")
            continue
        if "@" not in email or "." not in email:
            print("Invalid email format.")
            continue
        return email


def print_contacts(contacts) -> None:
    """
    Print contacts in formatted style.

    Args:
        contacts (list): List of contact dictionaries.
    """
    for c in contacts:
        print(f"{c['id']}. {c['name']} | {c['phone']} | {c['email']}")


def display_contact_book(contacts) -> None:
    """
    Display all contacts in the contact book.

    Args:
        contacts (list): List of contacts.
    """
    print("\nHere is your list of contacts:")
    print_contacts(contacts)


def create_new_contact(contacts: list[dict[str, str]]) -> None:
    """
    Create a new contact and add it to the list in-place.

    Args:
        contacts (list): Contact list to update.
    """
    name = validate_name()
    phone = validate_phone_num()
    email = validate_email()

    new_contact = {
        "id": len(contacts) + 1,
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)
    print("\nContact added successfully.")


def update_existing_contact(contacts: list[dict[str, str]]) -> None:
    """
    Update an existing contact in-place.

    Args:
        contacts (list): Contact list to modify.
    """
    display_contact_book(contacts)
    cid = select_contact_id(contacts)

    for c in contacts:
        if c["id"] == cid:
            print("Fields: name, phone, email")
            while True:
                field = input("Field to update: ").strip().lower()
                if field in ["name", "phone", "email"]:
                    break
                print("Invalid field.")
            if field == "name":
                c["name"] = validate_name()
            elif field == "phone":
                c["phone"] = validate_phone_num()
            elif field == "email":
                c["email"] = validate_email()
            print("Contact updated.")
            return


def delete_contact(contacts: list[dict[str, str]]) -> None:
    """
    Delete a contact in-place.

    Args:
        contacts (list): Contact list.
    """
    display_contact_book(contacts)
    cid = select_contact_id(contacts)

    for c in contacts:
        if c["id"] == cid:
            contacts.remove(c)
            print("Contact deleted.")
            return


def main() -> None:
    """
    Main application loop for the Contact Book CLI.

    Loads contacts, handles user actions, and saves
    changes to JSON on exit.
    """
    contacts = load_contact()

    while True:
        choice = get_user_input()

        if choice == "1":
            create_new_contact(contacts)
        elif choice == "2":
            display_contact_book(contacts)
        elif choice == "3":
            update_existing_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "q":
            with open("contacts.json", "w") as file:
                json.dump(contacts, file, indent=4)
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
