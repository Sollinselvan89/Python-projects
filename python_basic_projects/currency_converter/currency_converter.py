"""
Currency Converter
------------------
This program calculates value of target currency provided 
if an user provides the base currency and the total amount
"""

def calculate_currency_conversion(*,amount,base_rate, target_rate ): 
    """
    Calculate the the target currency amount using the base currency rate, 
    base currency amount and target currency.

    Parameters: 
        amount(float), base_rate(float), target_rate(float)

    Returns:
        float: calculated target amount


    """
    converted_amount = amount *(target_rate/base_rate) # amount = base currency amount
    return converted_amount

def currency_rates():
    """ 
    Maintains a dictionary of major currencies and their value

    Returns: 
        A dicionary with currency name as keys and currency rate as values 
        with USD as the base currency
    
    """
    currency_rates = {
    "USD": 1.00,     # US Dollar
    "EUR": 0.93,     # Euro
    "INR": 83.00,    # Indian Rupee
    "GBP": 0.79,     # British Pound
    "CAD": 1.36,     # Canadian Dollar
    "AUD": 1.52,     # Australian Dollar
    "JPY": 148.0,    # Japanese Yen
    "CHF": 0.89,     # Swiss Franc
    "CNY": 7.28,     # Chinese Yuan
    "AED": 3.67      # UAE Dirham
    }
    return currency_rates

def user_input():
    """
    Collects validated user inputs: base currency, target currency 
    and base amount

    Returns:
        tuple: amount, base_rate,target_rate,base,target

    """
    currency_rates_dic = currency_rates()
    currency_list = list(currency_rates_dic.keys())
    print(f"Available currencies for conversion: {currency_list}")
    
    while True:
        base = input("Please enter the base currency: ").upper().strip()
        if not base.isalpha():
             print("Please enter letters only")
             continue
        if base not in currency_list:
                print("Please choose a base currency from the list")
                continue
        base_rate = currency_rates_dic[base]
        break

    while True:
        target = input("Please enter the target currency: ").upper().strip()

        if not target.isalpha():
             print("Please enter letters only")
             continue
        if target == base:
             print("Target currency cannot be same as base currency")
             continue
        if target not in currency_list:
                print("Please choose a target currency from the list")
                continue
        target_rate = currency_rates_dic[target]
        break

    while True:
        amount_str = input("Please enter the base currency amount:").strip()
        try:
             amount = float(amount_str)
             if amount<1:
                print("Amount can not be zero or negative")
                continue
        except ValueError:
             print("Please enter a valid number")
        return amount, base_rate,target_rate,base,target

def main():
    """
    Main function to run the currency converter app
    """
    print("Welcome to the curreny converter app")
    amount, base_rate,target_rate,base,target = user_input()
    converted_amount = calculate_currency_conversion(amount, base_rate,target_rate)
    print(f"{base} {amount:.2f} = {target} {converted_amount:.2f}")
    print("Thank you for using the app")

if __name__=="__main__":
     main()


