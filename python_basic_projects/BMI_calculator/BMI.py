

def caculate_bmi(weight,height):
    bmi = weight/(height*height)
    return bmi


def get_input():

    while True:
        
        kgs_str = input("Enter your weight in kgs upto two decimals: ").strip()
        wt_str  = input("Enter the height in meters: ").strip()

        try:
            kgs = float(kgs_str)
            wt = float(wt_str)

            if kgs <=0 or wt <=0:
                print ("Values must be positive")
                continue

            if ('.' in kgs_str and len(kgs_str.split('.')[-1]) > 2) or \
                ('.' in wt_str and len(wt_str.split('.')[-1]) > 2):
                print("Use upto 2 decimals only")
                continue
        
        except ValueError:
            print("Enter numbers only")
            continue


        return kgs,wt

def main():
    print("Wecome to the BMI calculator app")
    kgs,wt = get_input()
    bmi = caculate_bmi(kgs,wt)

    if 18.5 <= bmi < 24.9:
        print(f"Your BMI is {bmi} and you are within the BMI range")
    elif bmi < 18.50:
        print(f"Your BMI is {bmi} and you are underweight")
    else:
        print(f"Your BMI is {bmi} and you are overweight the BMI range")
        

if __name__ == "__main__":
    main()
    