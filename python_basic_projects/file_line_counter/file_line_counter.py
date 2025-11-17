def get_user_input():
    """Prompt user for a file name and return the number of lines in it."""
    while True:
        file_location = input("Enter the name of your file: ").strip()

        if not file_location:
            print("File location cannot be empty")
            continue

        try:
            count = 0
            with open(file_location, "r") as file:
                for line in file:
                    count += 1

        except FileNotFoundError:
            print("File not found!")
            continue

        return count


def main():
    """Run the line counter program."""
    number_of_lines = get_user_input()
    print(f"The number of lines in the given file is {number_of_lines}")


if __name__ == "__main__":
    main()
