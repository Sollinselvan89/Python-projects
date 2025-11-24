"""
A simple CLI-based multiple-choice quiz program.
It displays each question with options, validates user input,
tracks correct and wrong answers, and shows final accuracy.
"""

from typing import List, Dict


QUIZ_DATA: List[Dict[str, str | list[str]]] = [
    {
        "question": "1. What is the correct file extension for Python files?",
        "options": ["a) .py", "b) .pyt", "c) .pt", "d) .python"],
        "answer": "a",
    },
    {
        "question": "2. Which keyword is used to create a function in Python?",
        "options": ["a) func", "b) method", "c) def", "d) create"],
        "answer": "c",
    },
    {
        "question": "3. What is the output of: print(3 * 2)?",
        "options": ["a) 32", "b) 6", "c) 3x2", "d) Error"],
        "answer": "b",
    },
    {
        "question": "4. Which symbol is used for comments in Python?",
        "options": ["a) //", "b) <!-- -->", "c) #", "d) /* */"],
        "answer": "c",
    },
    {
        "question": "5. What data type is this: [1, 2, 3]?",
        "options": ["a) Tuple", "b) Dictionary", "c) Set", "d) List"],
        "answer": "d",
    },
    {
        "question": "6. What is the output of: len('Python')?",
        "options": ["a) 5", "b) 6", "c) 7", "d) Error"],
        "answer": "b",
    },
    {
        "question": "7. Which operator is used for exponentiation?",
        "options": ["a) ^", "b) **", "c) x", "d) pow"],
        "answer": "b",
    },
    {
        "question": "8. What is the correct way to create a variable?",
        "options": ["a) var x = 10", "b) let x = 10", "c) x = 10", "d) int x = 10"],
        "answer": "c",
    },
    {
        "question": "9. Which function converts input to an integer?",
        "options": ["a) str()", "b) int()", "c) float()", "d) input()"],
        "answer": "b",
    },
    {
        "question": "10. What is the result of: 10 % 3?",
        "options": ["a) 3", "b) 1", "c) 0", "d) 2"],
        "answer": "b",
    },
]


def ask_questions(questions: dict) -> str | int:
    """Displays a single quiz question, gets user input, and returns result."""
    print(questions["question"])

    for option in questions["options"]:
        print(option)

    choice_list = ["a", "b", "c", "d", "q"]

    while True:
        user_ans = input(
            "Enter your choice (a/b/c/d) or q to quit: "
        ).strip().lower()

        if user_ans not in choice_list:
            print("Please enter a valid choice.")
            continue

        if user_ans == "q":
            return "q"

        if user_ans != questions["answer"]:
            return 0

        return 1


def run_quiz() -> None:
    """Runs the quiz loop, tracks score, and displays final results."""
    correct = 0
    wrong = 0

    for question in QUIZ_DATA:
        answer = ask_questions(question)

        if answer == "q":
            break

        if answer == 1:
            correct += 1
        else:
            wrong += 1

    print(f"Number of questions answered: {correct + wrong}")
    print(f"Correctly answered: {correct}")
    print(f"Wrongly answered: {wrong}")
    print(f"Accuracy: {(correct / (correct + wrong)) * 100:.2f}")
    

if __name__ == "__main__":
    run_quiz()
