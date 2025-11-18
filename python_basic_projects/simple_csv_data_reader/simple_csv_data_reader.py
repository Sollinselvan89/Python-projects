"""
Simple CSV Data Reader: Display and filter student records from a CSV file.
"""

import csv


def get_user_input() -> str:
    """Return a valid CSV file path entered by the user."""
    while True:
        file_location = input("Enter the location of your file: ").strip()

        if not file_location:
            print("File location cannot be empty.")
            continue

        try:
            with open(file_location, "r"):
                pass
            return file_location
        except FileNotFoundError:
            print("File not found! Please try again.")


def display_csv_pretty(filename: str) -> None:
    """Display all student records in formatted style."""
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row.get("name", "").strip()
            age = row.get("age", "").strip()
            grade = row.get("grade", "").strip()

            print(f"Name: {name} | Age: {age} | Grade: {grade}")


def filter_age_above_15(filename: str) -> None:
    """Display students with age > 15."""
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        print("Students with age > 15:")
        for row in reader:
            age = row.get("age", "").strip()

            if not age.isdigit():
                continue

            if int(age) > 15:
                name = row.get("name", "").strip()
                grade = row.get("grade", "").strip()
                print(f"Name: {name} | Age: {age} | Grade: {grade}")


def filter_grade_A(filename: str) -> None:
    """Display students whose grade is A."""
    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        print("Students with Grade == A:")
        for row in reader:
            grade = row.get("grade", "").strip().upper()

            if grade == "A":
                name = row.get("name", "").strip()
                age = row.get("age", "").strip()
                print(f"Name: {name} | Age: {age} | Grade: {grade}")


def get_filter_choice() -> int:
    """Return the user's menu selection."""
    print("\nChoose a filter:")
    print("1. Show all students")
    print("2. Age > 15")
    print("3. Grade == A")
    print("4. Quit")

    while True:
        choice = input("Enter your choice (1-4): ").strip()

        try:
            choice = int(choice)
            if choice not in range(1, 5):
                print("Enter a value from 1 to 4.")
                continue
            return choice
        except ValueError:
            print("Please enter numbers only.")


def run_menu(filename: str) -> None:
    """Run interactive menu based on user input."""
    while True:
        choice = get_filter_choice()

        if choice == 1:
            display_csv_pretty(filename)
        elif choice == 2:
            filter_age_above_15(filename)
        elif choice == 3:
            filter_grade_A(filename)
        elif choice == 4:
            print("Goodbye!")
            break


def main() -> None:
    """Program entry point."""
    filename = get_user_input()
    run_menu(filename)


if __name__ == "__main__":
    main()
