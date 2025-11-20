import os
import csv

def get_file_path() -> str:
    """Ask a user for a file path and validate its existence"""
    while True:
        file_path = input("Please enter the file path here:").strip()

        if not file_path:
            print("File path cannot be empty")
            continue

        if os.path.isfile(file_path):
            return file_path
        
        print("File not found! Please try again")


def preprocess_lines(file_path):
    
    with open(file_path, "r") as file:
        raw_lines = file.readlines()

    cleaned_lines = []
    for line in raw_lines:
        stripped = line.strip()

        if not stripped:
            continue

        if stripped.startswith("#"):
            continue

        cleaned_lines.append(stripped)
    
    return cleaned_lines

def tokenize_row(line:str) -> str:
    """
    Split a CSV line into exactly four fields or return None if invalid"
    """
    parts = line.split(",")

    if len(parts) != 4:
        return None
    
    parts = [p.strip() for p in parts]
    return parts

def normalize_name(name_str:str) -> tuple[str | None ,str]:
    """
    Normalize the name field and return (clean_name, status)
    """
    cleaned = name_str.strip()
    cleaned = " ".join(cleaned.split())

    if cleaned == "":
        return "" , "warning"
    
    if not any(c.isalpha() for c in cleaned):
        return None, "invalid"
    
    cleaned = cleaned.title()

    return cleaned, "ok"

def normalize_age(age_str:str) -> tuple[int | None, str]:
    """
    Normalize age field and return (clean_age, status)
    """
    cleaned = age_str.strip()

    if cleaned == "" or cleaned.upper() == "N/A":
        return None, "warning"
    
    words_to_numbers = {
        "five": 5, "six": 6, "seven": 7, "eight": 8,
        "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
        "thirteen": 13, "fourteen": 14, "fifteen": 15,
        "sixteen": 16, "seventeen": 17, "eighteen": 18,
        "nineteen": 19, "twenty": 20
    }

    lower_cleaned = cleaned.lower()
    if lower_cleaned in words_to_numbers:
        return words_to_numbers[lower_cleaned], "ok"
    
    if cleaned.isdigit():
        age= int(cleaned)
    else:
        return None, "warning"
    
    if not 5<= age <= 20:
        return age, "warning"
    
    return age, "ok"

def normalize_grade(grade_str:str) -> tuple[str | None , str]:
    """
    Normalize grade field and return (cleaned_grade, status)
    """
    cleaned = grade_str.strip()

    if cleaned == "":
        return None, "warning"
    
    cleaned = cleaned.upper()

    valid_grades = {
        "A", "A+", "A-",
        "B", "B+", "B-",
        "C", "D", "F"
    }

    if cleaned in valid_grades:
        return cleaned, "ok"
    
    return None, "invalid"

def normalize_email(email_str:str) -> tuple[str | None, str]:
    """
    Normalize email field and return (cleaned_email, status)
    """
    cleaned = email_str.strip().lower()

    if cleaned == "":
        return None, "warning"
    
    if cleaned.count("@") != 1:
        return None, "warning"
    
    user, domain = cleaned.split("@",1)
    if user == "" or domain =="":
        return None, "warning"
    
    if "." not in domain:
        return None, "warning"
    
    return cleaned, "ok"

def process_rows(tokenized_rows: list[list[str] | None]) -> tuple[
    list[dict], list[dict], list[dict]
]:
    """Process tokenized rows and classify them into clean, warning, or invalid."""

    clean_rows = []
    warning_rows = []
    invalid_rows = []

    for row in tokenized_rows:

        if row is None:
            invalid_rows.append({
                "original": "",
                "reason": "tokenization error"
            })
            continue

        raw_name, raw_age, raw_grade, raw_email = row

        clean_name, name_status = normalize_name(raw_name)
        clean_age, age_status = normalize_age(raw_age)
        clean_grade, grade_status = normalize_grade(raw_grade)
        clean_email, email_status = normalize_email(raw_email)

        statuses = {
            "name": name_status,
            "age": age_status,
            "grade": grade_status,
            "email": email_status
        }

        if "invalid" in statuses.values():
            invalid_fields = [field for field, status in statuses.items() if status == "invalid"]
            reason = "invalid: " + ", ".join(invalid_fields)

            invalid_rows.append({
                "original": ",".join([raw_name, raw_age, raw_grade, raw_email]),
                "reason": reason
            })
            continue

        if "warning" in statuses.values():
            warning_fields = [field for field, status in statuses.items() if status == "warning"]
            reason = "warning: " + ", ".join(warning_fields)

            warning_rows.append({
                "name": clean_name,
                "age": clean_age,
                "grade": clean_grade,
                "email": clean_email,
                "reason": reason
            })
            continue

        clean_rows.append({
            "name": clean_name,
            "age": clean_age,
            "grade": clean_grade,
            "email": clean_email
        })

    return clean_rows, warning_rows, invalid_rows


def write_output(
    clean_rows: list[dict],
    warning_rows: list[dict],
    invalid_rows: list[dict]
) -> None:
    """Write cleaned, warning, and invalid rows to CSV files."""

    # Write clean rows
    with open("cleaned.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "grade", "email"])
        for row in clean_rows:
            writer.writerow([row["name"], row["age"], row["grade"], row["email"]])

    # Write warning rows
    with open("warnings.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "age", "grade", "email", "reason"])
        for row in warning_rows:
            writer.writerow([
                row["name"],
                row["age"],
                row["grade"],
                row["email"],
                row["reason"]
            ])

    # Write invalid rows
    with open("invalid.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["original", "reason"])
        for row in invalid_rows:
            writer.writerow([row["original"], row["reason"]])

def main() -> None:
    """Run the CSV cleaning program."""

    file_path = get_file_path()
    lines = preprocess_lines(file_path)

    tokenized = []
    for line in lines:
        tokenized.append(tokenize_row(line))

    clean_rows, warning_rows, invalid_rows = process_rows(tokenized)

    write_output(clean_rows, warning_rows, invalid_rows)

    print(f"Clean rows: {len(clean_rows)}")
    print(f"Warning rows: {len(warning_rows)}")
    print(f"Invalid rows: {len(invalid_rows)}")

if __name__ == "__main__":
    main()

