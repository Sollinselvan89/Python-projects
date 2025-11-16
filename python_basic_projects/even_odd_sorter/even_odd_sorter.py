"""A simple script that separates user-entered numbers into even and odd lists."""

def get_user_input() -> list:
    """Return a list of whole numbers entered by the user."""
    while True:
        user_input = input("Please enter only whole numbers separated by commas: ")
        items = user_input.split(",")

        # Clean and filter out empty entries
        item_list = [item.strip() for item in items if item.strip()]

        if not item_list:
            print("The list cannot be empty. Enter at least one.")
            continue

        numbers = []
        try:
            for item in item_list:
                number = int(item)
                numbers.append(number)
        except ValueError:
            print("Whole numbers only.")
            continue

        return numbers


def sort_add_even(numbers: list) -> tuple[list, list]:
    """Return even and odd numbers separated into two lists."""
    odd = []
    even = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return even, odd


def main():
    """Run the even/odd sorter program."""
    print("Welcome to the even/odd sorter script")
    numbers = get_user_input()
    even, odd = sort_add_even(numbers)

    if not odd:
        print("There are no odd numbers in the list.")
        print(f"Even numbers: {even}")

    if not even:
        print("There are no even numbers in the list.")
        print(f"Odd numbers: {odd}")

    if odd and even:
        print(f"Odd numbers: {odd}")
        print(f"Even numbers: {even}")


if __name__ == "__main__":
    main()
