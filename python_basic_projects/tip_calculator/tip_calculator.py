
def tip_calculator(bill, tip_percentage): # bill is the total bill, tip_percentage is the percentage of the tip
    tip = bill * tip_percentage 
    return tip 

def bill_input(prompt): # prompt is the prompt for the bill input
    bill = input(prompt).strip()

    while True: 
        if not bill.isdigit():
            print("Please enter a valid number")
        
        else:
            return float(bill)
    
def tip_percentage():
    """Takes tip % as input"""
    print(f"0: No tip \n1 - 5%  \n2 - 10 %  \n 3 - 15% \n 4 - 20%")
    tip_choice = input("Please choose how much you want to tip:")
    while True:
        if not tip_choice.isdigit():
            print("Please enter a valid number")
        
        num = int(tip_choice)
        if num not in range(0,5):
            print("Please enter a valid number")    
        elif num == 0:
            return 1.0 
            break  
        elif num ==1:
            return 1.05
            break
        elif num ==2:
            return 1.1
            break
        elif num ==3:
            return 1.15
            break
        elif num ==4:
            return 1.2
            break
    
def main():
    print("Welcome to the tip_calculator app")

    bill = bill_input("Please enter the bill amount")

    tip_perc = tip_percentage() 

    final_bill = tip_calculator(bill,tip_perc)

    print(f"Here is your final bill: {final_bill} $")
    print("Thank you come again!")

if __name__ == "__main__":
    main()

        



            





   


    
    