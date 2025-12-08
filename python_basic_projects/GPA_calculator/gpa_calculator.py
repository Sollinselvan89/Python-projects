"""
GPA Calculator
--------------
This program calculates a student's Grade Point Average (GPA)
for one semester based on the number of subjects, their grades,
and corresponding credit hours.
"""

# correction: added top-level docstring to describe the program purpose clearly (PEP 8 recommends module docstrings)


def calculate_gpa(grade_credit_sum, credit_sum):
    """
    Calculate the GPA using the total grade-credit sum and total credits.

    Parameters:
        grade_credit_sum (float): Sum of (grade × credit) for all subjects.
        credit_sum (float): Sum of all credit hours.

    Returns:
        float: Calculated GPA value.
    """
    # correction: renamed function from 'caculate_gpa' → 'calculate_gpa' (typo fix and readability)
    gpa = grade_credit_sum / credit_sum
    return gpa


def user_input():
    """
    Collect validated user inputs for grades and credits of each subject.

    Returns:
        tuple: grade_credit_sum (float), credit_sum (float)
    """
    grade_credit_sum = 0.0 # initialize
    credit_sum = 0.0 # initialize

    while True:
        subjects_str = input("Hi, please enter the number of subjects: ").strip()
        try:
            subjects_cnt = int(subjects_str)
            if subjects_cnt not in range(1, 8):
                print(
                    "Please enter a valid subject count. "
                    "Each semester has a maximum of 7 subjects."
                )
                continue
            break
        except ValueError:
            print("Please enter a valid integer value.")
            # correction: changed error message to clarify input type (integer)

    print(f"\nYou will now enter grades and credits for {subjects_cnt} subjects.\n")

    for subject in range(1, subjects_cnt + 1):
        # Grade input validation
        while True:
            grade_str = input(
                f"Enter the grade for subject {subject} (0.0 to 4.0): "
            ).strip()
            try:
                grade = float(grade_str)
                if not 0.0 <= grade <= 4.0:
                    print("Enter a valid grade from 0.0 to 4.0 (inclusive).")
                    continue
                break
            except ValueError:
                print("Only numeric values are allowed for grades.")

        # correction: adjusted range (0.0–4.0) and message for clarity (aligned logic & wording)

        # Credit input validation
        while True:
            credit_str = input(
                f"Enter the credit for subject {subject} (1–5): "
            ).strip()
            try:
                credit = float(credit_str)
                if not 1 <= credit <= 5:
                    print("Enter a valid credit from 1 to 5 (inclusive).")
                    continue
                break
            except ValueError:
                print("Only numeric values are allowed for credits.")

        # correction: changed int() → float() to allow 1.5, 2.5 credits; fixed wording consistency

        # Accumulate totals
        subject_total = grade * credit
        grade_credit_sum += subject_total
        credit_sum += credit

    return grade_credit_sum, credit_sum


def main():
    """Main function to run the GPA calculator."""
    print("Welcome to the GPA Calculator!")  # correction: fixed capitalization and grammar

    grade_credit_sum, credit_sum = user_input()
    gpa = calculate_gpa(grade_credit_sum, credit_sum)

    print(f"\nYour GPA for this semester is {gpa:.2f}")
    print("Thank you for using the GPA Calculator!")


if __name__ == "__main__":
    main()
