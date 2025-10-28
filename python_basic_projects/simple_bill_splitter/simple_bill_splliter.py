
""" This script calculates the total bill amount if an user gives 
the total amount, number of persons to split and the tip %
"""
def get_user_input() -> tuple[float, int, float] :
    """Gets user input such as amount, tip % and split number"""
    while True:
        bill_amount_str = input(
             "Enter the total bill amount upto 2 decimals: "
             ).strip()
        try:
            bill_amount = float(bill_amount_str)
            if (bill_amount < 0):
                 print("Please enter a valid number")
                 continue
            elif "." in bill_amount_str and len(bill_amount_str.split(".")[1] )> 2:
                 print("Please enter no more than two decimal places.")
                 continue
            break
        except ValueError:
             print("Enter a valid number")
             
    tip = 0
    while True:
        tip_choice = input("Do you want to offer a tip: Y/N: ").strip().lower()
        if tip_choice not in ('y', 'n'):
            print("Enter either Y or N")
            continue
        break

    if tip_choice == 'y':
        while True:
            tip_str= input("Enter the tip % (1-25):").strip()
            try:
                tip = float(tip_str)
                if not 0<tip<26:
                    print("Enter the tip % 1-25")
                    continue
                elif "." in tip_str and len(tip_str.split(".")[1] )> 2:
                    print("Please enter no more than two decimal places.")
                    continue
                break
            except ValueError:
                print("Numbers only")

    
    split_num = 0
    while True:
        split_choice = input("Do you want to split: Y/N: ").strip().lower()
        if split_choice not in ('y', 'n'):
            print("Enter either Y or N")
            continue
        break

    if split_choice == 'y':
        while True:
            split_num_str = input("Please enter the number:")
            try:
                split_num = int(split_num_str)
                if split_num < 0 :
                    print("Please enter a positive whole number.")
                    continue
                break
            except ValueError:
                print("Numbers only, please")
    
    return bill_amount,split_num,tip


def calculate_bill_amount(*,bill_amount:float,split_num:int,tip:float) -> tuple[float,float]:
    """Calculates and returns the total bill amount"""
    if split_num>0:
            total_bill = (bill_amount * ((100+tip)/100))
            per_person = total_bill/split_num
    elif split_num == 0:
        total_bill = (bill_amount * ((100+tip)/100))
        per_person = total_bill
    return total_bill, per_person

def main():
    print("Wecome to the bill splitter app")
    bill_amount,split_num,tip = get_user_input()
    total_amount,per_person = calculate_bill_amount(
        bill_amount=bill_amount,
    split_num=split_num,
    tip=tip
        )

    print("======================BILL SUMMARY======================")

    if split_num == 0:
        if tip == 0:
            print(f"Your total bill is {total_amount:.2f} with no tips ")
        elif tip >0:
            print(
                f"Your total bill is {total_amount:.2f},"
                f"with a tip percentage of {tip}%")
    elif split_num > 0:
        if tip ==0:
            print(
            f"Your total bill is {total_amount:.2f},"
            f"It is split across {split_num} persons."
            f"Bill per person is {per_person:.2f}"
              )
        elif tip > 0:
            print(
                f"Your total bill is {total_amount:.2f}, "
                f"split across {split_num} persons, "
                f"Bill per person is {per_person:.2f}"
                f"and your tip is {tip}."
                )
    print("Thank you for using the Bill Splitter app")

if __name__ == "__main__":
    main()





        






