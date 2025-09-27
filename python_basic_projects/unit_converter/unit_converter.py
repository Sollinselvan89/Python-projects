# unit_converter_final.py
print("Hello!")
print("Welcome to SSM's unit converters")
print("What do you want to convert to?\n")

# ---------- Conversion functions (pure math) ----------
def f_to_c(x):
    return (x - 32) * (5 / 9)

def c_to_f(x):
    return (x * (9 / 5)) + 32

def km_to_m(x):
    return x * 1000.0

def m_to_km(x):
    return x / 1000.0

def kg_to_gm(x):
    return x * 1000.0

def gm_to_kg(x):
    return x / 1000.0

# ---------- Input helpers ----------
def get_input(prompt):
    """
    Ask user for a number (allow decimals). Keeps asking until valid.
    Returns a float rounded to 2 decimals.
    """
    while True:
        s = input(prompt).strip()
        try:
            value = float(s)               # validate numeric
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 12 or 12.34).")
            continue

        # if there is an explicit decimal point in the typed string, count digits after it
        if "." in s:
            # handle cases like "12." -> split -> ["12", ""] -> decimals = 0 (acceptable)
            decimals = len(s.split(".", 1)[1])
            if decimals > 2:
                print("Please enter a number with at most 2 decimal places.")
                continue

        # valid input; store rounded to 2 decimals (you can remove round() if you want more precision)
        return round(value, 2)

def get_menu_choice(prompt, valid_range):
    """Get a validated integer menu choice within valid_range (an iterable of ints)."""
    valid_set = set(valid_range)
    while True:
        choice = input(prompt).strip()
        if not choice.isdigit():
            print("Please enter a number corresponding to the menu options.")
            continue
        n = int(choice)
        if n in valid_set:
            return n
        print("Choice out of range. Try again.")

# ---------- Main menu / wiring ----------
def main_menu():
    while True:
        print("\nMenu:")
        print("0) Quit")
        print("1) Fahrenheit -> Celsius")
        print("2) Celsius -> Fahrenheit")
        print("3) Kilometers -> Meters")
        print("4) Meters -> Kilometers")
        print("5) Kilograms -> Grams")
        print("6) Grams -> Kilograms")

        num = get_menu_choice("Enter your choice (0-6): ", range(0, 7))

        if num == 0:
            print("Thank you — come again!")
            break

        # get single numeric input AFTER user chooses conversion
        value = get_input("Enter the value to convert (decimals allowed, up to 2 dp): ")

        # call appropriate function, print result (rounded/displayed to 2 decimals)
        if num == 1:
            result = f_to_c(value)
            print(f"{value:.2f} °F  =  {result:.2f} °C")
        elif num == 2:
            result = c_to_f(value)
            print(f"{value:.2f} °C  =  {result:.2f} °F")
        elif num == 3:
            result = km_to_m(value)
            print(f"{value:.2f} km  =  {result:.2f} m")
        elif num == 4:
            result = m_to_km(value)
            print(f"{value:.2f} m   =  {result:.2f} km")
        elif num == 5:
            result = kg_to_gm(value)
            print(f"{value:.2f} kg  =  {result:.2f} g")
        elif num == 6:
            result = gm_to_kg(value)
            print(f"{value:.2f} g   =  {result:.2f} kg")

if __name__ == "__main__":
    main_menu()
