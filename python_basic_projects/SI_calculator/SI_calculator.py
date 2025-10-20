

def calculate_simple_interest(principal,rate,years):
    """This function gets input from main function and outputs SI"""
    simple_interest = (principal*years*rate)/100 # PNR/100
    total = principal +  simple_interest # Total amount: principal + Interest
    return simple_interest,total

def user_input():
        """Prompts for principal, rate, and years.
    Repeats until valid numeric inputs are entered."""
    
        while True:
            principal_str = input("Enter your prinicple amount:").strip()
            try:
                principal = float(principal_str)
                if principal < 0:
                    print("Please enter a valid amount!")
                    continue
                break
            except ValueError:
                print("Please enter numbers only")
             

        while True: 
            rate_str = input("Enter the interest rate in percentage:").strip()
            try:
                rate = float(rate_str) 
                if not (0<=rate<100):
                    print("Enter the rate  between 0 and 100")
                    continue
                break
            except ValueError:
                print("Enter a valid number")

        while True: 
            years_str = input("Enter the number of years:").strip()
            try:
                years = int(years_str)
                if not (0<years<100):
                    print("Enter the number of years between 0 and 100")
                    continue
                break
            except ValueError:
                print("Enter a valid number")
            

        print(f"You entered principal = {principal}, rate = {rate}%, years = {years}")
        return principal,rate,years

def main():
    print("Hi there! Welcome to the Simple Interest Calculator")
    principal,rate,years = user_input()
    simple_interest,total = calculate_simple_interest(principal,rate,years)

    print(f"The total amount principa amount +interest amount is Rs. {total:.2f}")
    print(f"Your interest amount for {years} years is Rs. {simple_interest:.2f}")
    print("Thank you for using the Simple Interest Calculator!")

if __name__=="__main__":
    main() 
        
        
        



    #handle errors
