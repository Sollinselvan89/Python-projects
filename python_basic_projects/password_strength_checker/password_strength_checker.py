"""
This script calculates the strength of a user's password and 
tells whether  the password is strong, intermediate or weak 
"""

def check_password_strength(
upper_case_cnt:int,
lower_case_cnt:int,
digit_cnt:int,
spcl_char_cnt:int) -> int:
    """Returns 'Strong', 'Intermediate', or 'Weak' based on character mix."""
    lis_count = [upper_case_cnt,lower_case_cnt,digit_cnt,spcl_char_cnt]
    cnt = 0
    for count in lis_count:
        if count > 0:
            cnt += 1
    
    if cnt ==4:
        return "Strong"
    elif cnt==3:
        return "Intermediate"
    else:
        return "Weak"
    

def calculate_password_strength(password: str) -> int:
    """Calculates the strength of the entered password"""
    upper_case_cnt = 0
    lower_case_cnt = 0
    digit_cnt      = 0
    spcl_char_cnt = 0
    for letter in password:
        if letter.isupper():
            upper_case_cnt +=1
        elif letter.islower():
            lower_case_cnt +=1
        elif letter.isdigit():
            digit_cnt += 1
        else: 
            spcl_char_cnt +=1
    return upper_case_cnt,lower_case_cnt,digit_cnt,spcl_char_cnt 
        

def get_userinput() -> str:
    """Gets password from the user"""
    print("Please enter the password of your choice")
    print("Minimum length:8 characters")
    print("Atleast one uppercase, one lowercase, one digit and one special character")
    

    while True:
        pass_str= input("Enter the password:")
        if len(pass_str) < 8:
            print("The length of the password is less than 8 charcters")
            print("Enter at least password with atleast 8 characters")
            continue
        break 
    return pass_str


def main():
    print("Wecome to the Password Strength Checker")
    password = get_userinput()
    upper_case_cnt,lower_case_cnt,digit_cnt,spcl_char_cnt = (
        calculate_password_strength(password)
    )
    strength = check_password_strength(
        upper_case_cnt,lower_case_cnt,digit_cnt,spcl_char_cnt
    )

    print(f"The current strength of your password is {strength}")


if __name__=="__main__":
    main()

