import json

def load_contact() -> list[dict[str, str]]:
    """Load contacts from JSON and assign IDs."""
    try:
        with open("contacts.json", "r") as file:
            without_id = json.load(file)
            count = 0
            for contact in without_id:
                count += 1
                contact["id"] = count
            with_id_list = without_id
        return with_id_list
    except FileNotFoundError:
        print("json file not found. Created an empty json file")
        with open("contacts.json", "w") as file:
            json.dump([], file, indent=4)
        return []


def get_user_input():
    """Display menu and return user's option."""
    print("Want you want to do with the contact list")
    print("Please select from the following options:")
    print(
        f"1 -> Create new contact\n"
        f"2 -> View the contact book\n"
        f"3 -> Update the contact book\n"
        f"4 -> Delete a contact\n"
        f"q -> To quit\n"
    )

    while True:
        user_input_str = input("Enter your choice 1-4 or q: ").strip().lower()

        if user_input_str not in ["1", "2", "3", "4", "q"]:
            print("Please enter a valid choice")
            continue
        return user_input_str


def select_contact_id(contacts) -> int:
    """Ask user to choose a contact ID."""
    while True:
        contact_id_str = input("Select the contact number to update: ")

        if not contact_id_str:
            print("This field  cannot be empty")
            continue

        try:
            contact_id = int(contact_id_str)
            if contact_id not in range(0, len(contacts) + 1):
                print("Number you have entered is not in range")
                continue
        except ValueError:
            print("Please enter a valid number")
        
        return contact_id


def validate_name(contact: dict) -> str:
    """Validate and return a formatted name."""
    while True:
        name = input("New name: ").strip().lower()
        if not name:
            print("name field cannot be empty")
            continue
        if any((char.isdigit() or char.isnumeric()) for char in name):
            print("names cannot have numbers or symbols")
            continue
        
        return name.title()


def validate_phone_num(contact: dict) -> str:
    """Validate and return a phone number."""
    while True:
        phone_num = input("Please enter the phone number: ").strip()
        if not phone_num:
            print("phone number cannot be empty")
            continue

        if not 7 <= len(phone_num) <= 15:
            print("The length of the phone number should be between 7-15")
            continue
        
        try:
            phone_num = int(phone_num)
            break
        except ValueError:
            print("Only whole numbers please")
        
    return phone_num


def validate_email(contact: dict) -> str:
    """Validate and return an email."""
    while True:
        email = input("Please enter the email: ").strip().lower()

        if not email:
            print("email cannot be empty")
            continue
        
        email_list = list(email.split("@"))
        if "@" not in email or "." not in email:
            print("Invalid email")
            print("Please enter a valid email")
            continue
        
        return email


def print_contacts(contacts_list) -> None:
    """Print contacts in formatted layout."""
    for contact in contacts_list:
        print(f"{contact['id']}.{contact['name']} | {contact['phone']} | {contact['email']}")


def display_contact_book(contacts_list) -> list[dict[str, str]]:
    """Show all contacts in the contact book."""
    print("Here is your list of contacts")
    for contact in contacts_list:
        print(
            f"{contact['id']}."
            f"{contact['name']} | {contact['phone']} | {contact['email']}"
        )

    return contacts_list


def create_new_contact(contacts_list: list[dict[str, str]]) -> list[dict[str, str]]:
    """Create a new contact (in-place mutation)."""
    contacts = display_contact_book(contacts_list=contacts_list)
    new_contact = {}
    name = validate_name(contact=new_contact)
    phone_num = validate_phone_num(contact=new_contact)
    email = validate_email(contact=new_contact)
    new_contact["name"] = name
    new_contact["phone"] = phone_num
    new_contact["email"] = email
    new_contact["id"] = (len(contacts) + 1)
    contacts.append(new_contact)
    print(contacts)
    return contacts


def update_existing_contact(
    contacts_list: list[dict[str, str]]
) -> list[dict[str, str]]:
    """Update an existing contact (in-place mutation)."""

    contacts = display_contact_book(contacts_list=contacts_list)
    print("Select the id of the contact which you want to update")
    contact_id = select_contact_id(contacts=contacts)

    for contact in contacts:
        if int(contact["id"]) == contact_id:
            print("Available fields Name, Age and Email")
            while True:
                field = input("Enter the field you want to update:").strip().lower()
                
                if field not in ["name", "age", "email"]:
                    print("Only these three fields are the permitted fields")
                    continue
                break

            if field == "name":
                name = validate_name(contact=contact)
                contact["name"] = name
                break
            elif field == "phone":
                phone_num = validate_phone_num(contact=contact)
                contact["phone"] = phone_num
                break
            elif field == "email":
                email = validate_email(contact=contact)
                contact["email"] = email
                break

    return contacts


def delete_contact(contacts_list: list[dict[str, str]]) -> list[dict[str, str]]:
    """Delete a contact (in-place mutation)."""
    contacts = display_contact_book(contacts_list=contacts_list)
    print("Select the id of the contact you want to delete:")
    contact_id = select_contact_id(contacts=contacts)

    for contact in contacts:
        if contact["id"] == contact_id:
            contacts.remove(contact)
            for key, value in contact.items():
                print(f"Deleted contact: {key}:{value}\n")

    return contacts


def main():
    """Main loop for the contact book application."""
    contact_list = load_contact()

    while True:
        user_choice = get_user_input()
        if user_choice == "q":
            print("quitting")
            print("Thank You!")

            with open("contacts.json", "w") as file:
                json.dump(contact_list, file, indent=4)
            break
        
        elif user_choice == "1":
            updated_contacts_new = create_new_contact(contacts_list=contact_list)
            print("Here is your updated contacts list with a new contact ")
            print_contacts(contacts_list=updated_contacts_new)
            contact_list = updated_contacts_new

        elif user_choice == "2":
            display_contact_book(contacts_list=contact_list)

        elif user_choice == "3":
            updated_contacts_edited = update_existing_contact(
                contacts_list=contact_list
            )
            print("Here is your updated contacts list with the edit")
            print_contacts(contacts_list=updated_contacts_edited)
            contact_list = updated_contacts_edited

        elif user_choice == "4":
            updated_contacts_deleted = delete_contact(
                contacts_list=contact_list
            )
            print_contacts(contacts_list=updated_contacts_deleted)
            contact_list = updated_contacts_deleted


if __name__ == "__main__":
    main()
