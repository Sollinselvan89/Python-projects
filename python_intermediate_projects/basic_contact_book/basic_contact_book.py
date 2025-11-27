import json

def load_contact()-> list:

    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("json file not found. Created an empty json file")
        with open("contacts.json", "w") as file:
            json.dump([], file, indent=4)
        return []


def get_user_input():
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

        if user_input_str not in ["1", "2", "3", "4","q"]:
            print("Please enter a valid choice")
            continue
        print(type(user_input_str))
        return user_input_str
    
def create_new_contact(contacts:list):
    while True:
        name = input("Please enter the name: ").strip().lower()
        if not name:
            print("name field cannot be empty")
            continue
        if any((char.isdigit() or char.isnumeric()) for char in name):
            print("names cannot have numbers or symbols")
            continue

        break
    
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
        except ValueError:
            print("Only whole numbers please")
        
        break

    while True:

        email = input("Please enter the phone number: ").strip()

        if not email:
            print("email cannot be empty")
            continue
        
        email_list = list(email.split("@"))
        if "@" not in email or "." not in email:
            print("Invalid email")
            print("Please enter a valid email")
            continue
        break
    new_contact ={}
    new_contact["name"] = name 
    new_contact["phone"] = phone_num
    new_contact["email"] = email
    contacts.append(new_contact)

    print(contacts)
    return contacts

def update_existing_contact(contacts:list):
    print("Here is your list of contacts")

    count=0
    for contact in contacts:
            count += 1
            contact["id"] = count
            print(f"{contact["id"]}. {contact["name"]} | {contact["phone"]} | {contact["email"]}")
    while True:
        contact_id_str = input("Select the contact number to update: ")

        if not contact_id_str:
                print("This field  cannot be empty")
                continue

        try:
            contact_id = int(contact_id_str)
            if contact_id not in range(0, len(contacts)+1):
                print("Number you have entered is not in range")
                continue
        except ValueError:
            print("Please enter a valid number")

        for contact in contacts:
            if contact["id"] == contact_id:
                print(
                    "Available fields Name, Age and Email"
                )
                while True:
                    field = input(
                    "Enter the field you want to update:"
                    ).strip().lower()
                    
                    if field not in ["name","age","email"]:
                        print("Only these three are the permitted fields")
                        continue
                    break

                if field == "name":
                    while True:
                        name = input("New name: ").strip().lower()
                        if not name:
                            print("name field cannot be empty")
                            continue
                        if any((char.isdigit() or char.isnumeric()) for char in name):
                            print("names cannot have numbers or symbols")
                            continue
                        contact["name"] = name
                        return contact
                elif field == "age":    
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
                        except ValueError:
                            print("Only whole numbers please")
                        
                        contact["phone"] = phone_num
                        return contact
                elif field == "email":

                    while True:

                        email = input("Please enter the phone number: ").strip()

                        if not email:
                            print("email cannot be empty")
                            continue
                        
                        email_list = list(email.split("@"))
                        if "@" not in email or "." not in email:
                            print("Invalid email")
                            print("Please enter a valid email")
                            continue
                        contact["email"] = email
                        return contact
                                    

def display_contact_book(contacts):
    for contact in contacts:
            print(f"{contact["name"]} | {contact["phone"]} | {contact["email"]}")
    
def main():
    contact_list = load_contact()
    
    while True:
        user_choice = get_user_input()
        if user_choice == "q":
            print("quitting")
            return
        elif user_choice == "1":
            create_new_contact(contacts=contact_list)
        elif user_choice == "2":
            update_existing_contact(contacts=contact_list)
        elif user_choice == "3":
            pass
        elif user_choice == "4":
            pass
    

if __name__ == "__main__":
    main()




