""" 
This App helps to split bills between people based on the contribution made 
by each person.
"""  # correction: Use lowercase 'app' and clarify purpose — e.g., "This app splits a shared bill based on each person's contribution."


def get_user_input() -> dict:
    """Gets user input and stores in a dictionary and ouputs a dictionary 
    with person name and the respective amount"""
    # correction: "Outputs" → "returns"; fix typos and clarity.
    # Suggested: """Collects user inputs for each person and returns a dictionary
    # mapping each person's name to their contribution amount."""
    print("Between how many persons you want to split the bill?")

    while True:
        persons_str = input("Enter the count:").strip()

        try:
            persons_count = int(persons_str)
            if persons_count < 0:
                print("Please enter only positive whole numbers")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number greater than zero")

    persons_contributions = {}
    for x in range(1, persons_count + 1):
        while True:
            person_key = input(
                f"Please enter the person number{x} name "
            ).strip()
            person_key = " ".join(person_key.split())  # Normalize spaces

            if not person_key:
                print("Name cannot be empty")
                continue
            elif not (2 <= len(person_key) <= 30):
                print("Name must be between 2 and 30 charcters")
                # correction: Typo → "characters"
            elif not person_key.replace(" ", "").isalpha():
                print("Please enter letters only.")
                continue
            else:
                person_key = person_key.title()
                break

        while True:
            print(f"Hello {person_key}! ")
            amount_str = input(
                "Please enter the amount upto 2 decimal places:"
            )

            try:
                amount = float(amount_str)
                if amount < 0:
                    print("Amount can not be less than zero")
                    continue
                elif '.' in amount_str and len(amount_str.split('.')[-1]) > 2:
                    print("Please enter only upto two decimals")
                    # correction: "upto" → "up to"
                    continue
                persons_contributions[person_key] = amount
                break
            except ValueError:
                print("Please enter a valid number")

    return persons_contributions


def calculate_settlement(contributions: dict) -> dict:
    """Gets details of persons and respective contribution and gives out 
    settlement amount for each person.
    """
    # correction: Improve grammar and precision.
    # Suggested: """Calculates how much each person owes or should receive
    # based on their contribution compared to the equal share."""
    total_amount = sum(contributions.values())
    num_people = len(contributions)
    equal_share_amount = total_amount / num_people
    settlement = {}
    for person, amount in contributions.items():
        settlement[person] = round(amount - equal_share_amount, 2)
    return settlement


def display_settlement(settlement):
    """Shows output of settlement in a proper format: 
    who receives, who owes and who is settled up
    """
    # correction: Clarify docstring with complete sentences and correct punctuation.
    # Suggested: """Displays the final settlement summary showing who should
    # receive money, who owes money, and who is already settled."""
    print("====== Final Settlments Summary ======")
    # correction: Typo → "Settlements"
    for person, balance in settlement.items():
        if balance > 0:
            print(f"{person} should receive Rs. {balance:.2f}")
        elif balance < 0:
            print(f"{person} owes Rs.{abs(balance):.2f}")
        else:
            print(f"{person} is settled up.")


def main():
    print("Wecome to the bill splitter")
    # correction: Typo → "Welcome"
    contributions = get_user_input()
    settlement = calculate_settlement(contributions)
    display_settlement(settlement)


if __name__ == "__main__":
    main()
