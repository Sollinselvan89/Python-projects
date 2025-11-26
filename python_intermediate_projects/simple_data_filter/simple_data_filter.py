"""A simple CSV data filtering tool that lets users filter rows by numeric or string conditions and saves the result to a new CSV."""

import csv


def get_user_input() -> list[dict[str, str]]:
    """Gets a valid CSV path from the user and returns all rows as a list of dictionaries."""

    # Gets a valid CSV path from the user and returns all rows as dictionaries.
    while True:
        user_input = input("Enter the csv file's path: ").strip()
        

        if not user_input:
            print("Path cannot be empty")
            continue

        try:
            with open(user_input,"r", newline = "", encoding="utf-8") as file:
                reader = csv.DictReader(file)

                if reader.fieldnames is None:
                    print("CSV has a header but no data rows.")
                    continue

                rows = list(reader)
                if not rows:
                    print("CSV is empty")
                    continue
                print(rows)
                return rows
                
        except FileNotFoundError:
                print("File not found!")
                continue


def choose_column(rows: list[dict[str, str]]) -> str | int:
    """Asks the user to choose a column for filtering and returns the column name or 0 to quit."""

    print(rows[0].keys())
    print("Select the column by which you want to filter")

    while True:
        user_choice_str = input(
            f"Enter 0 to quit\n"
            f"Enter 1 for id column\n"
            f"Enter 2 for name column\n"
            f"Enter 3 for age column\n"
            f"Enter 4 for grade column\n"
            f"Enter 5 for city column: \n"
        )

        try: 
            user_choice =int(user_choice_str)
            if user_choice not in range(0,6):
                print("Please enter a valid choice")
                continue
            break
        except ValueError:
            print("Please enter only a valid choice")
        
    if user_choice == 0:
        return 0
    else:
        user_choice
        columns ={
                1:"id",
                2:"name",
                3:"age",
                4:"grade",
                5:"city"
            }

        return columns[user_choice].strip()


def choose_filter_mode(
    rows: list[dict[str, str]], 
    column_choosen: str
) -> tuple[list[dict[str, str]], str]:
    
    """Applies numeric or string-based filtering and returns the filtered rows and the user’s filter option."""


    filtered = []
    if column_choosen in ["age","id"]:
        print(
        "Select the filter you want to apply " 
        "along with a whole postive number >0:"
        )
        print("Example input: <=9, >=10, ==22, <99, >2")
        
        operators = ["<=", ">=", "==", "<", ">"]

        while True:
            user_choice_str =input("Enter your choice:").strip()

            if not user_choice_str:
                print("Choice cannot be empty")
                continue

            correct_choice = False
            for op in operators:
                if user_choice_str.startswith(op):
                    operator = op
                    num_part_str = user_choice_str[len(op):]
                    correct_choice = True
                    break
                
            if not correct_choice:
                print("Invalid operator")
                continue
            
            if not num_part_str:
                print("Enter a number along with the operator please")
                continue 

            try:
                num_part = int(num_part_str)
                if num_part <= 0:
                    print("The entered number should be > 0")
                    continue
                break
            except ValueError:
                print("Only positive whole numbers >0 please")
                continue
        
        if operator == "<=":
            for row in rows:
                if int(row[column_choosen]) <= num_part:
                    filtered.append(row)
        elif operator == ">=":
            for row in rows:
                if int(row[column_choosen]) >= num_part:
                    filtered.append(row)
        elif operator == "==":
            for row in rows:
                if int(row[column_choosen]) == num_part:
                    filtered.append(row)
        elif operator == "<":
            for row in rows:
                if int(row[column_choosen]) < num_part:
                    filtered.append(row)
        else: 
            for row in rows:
                if int(row[column_choosen]) > num_part:
                    filtered.append(row)
        
        return filtered, user_choice_str

    else:
        print("Select type of match you want to do:")
        print(f"Available options: \n 1.Exact match \n 2. Contains match)")

        valid_choices  = ["1","2"]
        while True:
            filter_choice_str = input(
                f"Enter 1 -> Option 1 \n 2 -> Option 2 "
                                    ).strip()
            
            if filter_choice_str not in valid_choices:
                print("Enter a valid choice: 1 or 2 ")
                continue
            break

        if filter_choice_str == "1":

            while True:
                user_word = input(
                            f"Enter the {column_choosen} you want to search: "
                            ).strip().lower()

                if not user_word:
                    print("This field cannot be left empty")
                    continue

                if any(char.isdigit() for char in user_word):
                    print("Only letters please")
                    continue

                for row in rows:
                    for key,value in row.items():
                        if key == column_choosen:
                            if value.lower() == user_word:
                                filtered.append(row)
                return filtered, user_word            

        elif filter_choice_str == "2":
            while True:
                user_word = input(
                    f"Enter the letters you want to search in {column_choosen} :"
                ).strip().lower()

                if not user_word:
                    print("Atleast one letter please.")
                    continue

                if any(char.isdigit() for char in user_word):
                    print("Only letters please")
                    continue

                for row in rows:
                    for key,value in row.items():
                        if key == column_choosen:
                            if  user_word in value.lower():
                                filtered.append(row)
                    
                return filtered, user_word  
            
def output_csv(filtered_rows: list[dict[str, str]]) -> None:
    """Writes the filtered rows to a new CSV file using the same headers."""
    fieldnames = filtered_rows[0].keys()
    with open(
        "filtered_output.csv", "w", 
        newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)


def main():
    print("Welcome to the basic filter app")
    rows = get_user_input()
    column_choice = choose_column(rows)

    if column_choice == 0:
        print("Thank you! Come again!")
        return
    else:
        column_choice
    
    filtered_columns,user_option  = choose_filter_mode(
                        rows=rows, 
                        column_choosen=column_choice
    )
    
    if not filtered_columns:
        print(
            f"There is not result for your filter {column_choice}:{user_option}"
        )
    elif filtered_columns:
        output_csv(filtered_columns)
        print(f"Your filter {column_choice}:{user_option}")
        print("Your filtered csv can be found in the root")
        print("Thank you for using the filter app")
    

if __name__ == "__main__":
    main()