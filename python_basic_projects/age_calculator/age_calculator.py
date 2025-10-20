import datetime

def calculate_age(dob): 
    today = datetime.date.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

def get_dob():
    today = datetime.date.today()
    while True:
        date_str = input("Enter your date of birth in dd-mm-yyyy format: ")
        try:
            dob = datetime.datetime.strptime(date_str.strip(), "%d-%m-%Y").date()
            if dob > today:
                print("DOB cannot be in the future. Please enter a past date.\n")
                continue
            # (Optional) sanity check for very old dates:
            if dob.year < 1900:
                print("That seems too old. Please re-enter a valid date.\n")
                continue
            return dob
        except ValueError:
            print("Invalid date. Please use dd-mm-yyyy (e.g., 05-11-1992).\n")

def main():
    dob = get_dob()
    age = calculate_age(dob)
    print(f"DOB:   {dob.strftime('%d-%m-%Y')}")
    print(f"Today: {datetime.date.today().strftime('%d-%m-%Y')}")
    print(f"Your current age is {age}")

if __name__ == "__main__":
    main()
