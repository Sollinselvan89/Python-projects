"""
Password Generator Application

Generates a secure password based on user-selected options.
"""

import random
import string


# Character sets (constants)
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
DIGITS = string.digits
PUNCTUATIONS = string.punctuation


def get_user_input() -> tuple[int, dict]:
    """Collect and validate password length and character type selections."""
    
    print("Passwords can have from 8 to 20 characters.")

    # Validate password length
    while True:
        pass_len_str = input(
            "Enter the number of characters you want for your password: "
        ).strip()

        try:
            pass_len = int(pass_len_str)
            if pass_len not in range(8, 21):
                print("Please enter values between 8 and 20.")
                continue
            break
        except ValueError:
            print("Numbers only please.")

    # Character type choices
    char_choices = ["upper_case", "lower_case", "digits", "punctuations"]
    char_choices_dict = {}

    while True:
        for choice in char_choices:
            while True:
                answer = input(f"Include {choice}? (y/n): ").strip().lower()
                if answer not in ["y", "n"]:
                    print("Please select either y or n only.")
                    continue
                char_choices_dict[choice] = answer
                break

        if all(val == "n" for val in char_choices_dict.values()):
            print("You must select at least ONE character type.\n")
            continue
        break

    return pass_len, char_choices_dict


def generate_password(pass_len: int, choices_dictionary: dict) -> str:
    """Generate a password using the selected character categories."""

    char_map = {
        "upper_case": UPPER_CASE,
        "lower_case": LOWER_CASE,
        "digits": DIGITS,
        "punctuations": PUNCTUATIONS,
    }

    pool = ""
    for key, value in choices_dictionary.items():
        if value == "y":
            pool += char_map[key]

    password_characters = [random.choice(pool) for _ in range(pass_len)]
    random.shuffle(password_characters)

    return "".join(password_characters)


def main():
    """Run the password generator workflow."""
    
    print("Welcome to the Password Generator App!")

    password_length, user_choices = get_user_input()
    password = generate_password(password_length, user_choices)

    print(f"\nHere is your generated password: {password}\n")


if __name__ == "__main__":
    main()
