PRODUCTS = { # why in upper?
    
    "tops": {
        "t-shirt": 30,
        "shirt": 50,
        "hoodie": 60,
        "sweater": 55
    },
    "bottoms": {
        "shorts": 20,
        "pants": 50,
        "jeans": 70,
        "joggers": 40
    },
    "footwear": {
        "sneakers": 80,
        "sandals": 35,
        "boots": 120
    },
    "accessories": {
        "cap": 10,
        "belt": 25,
        "socks": 5,
        "scarf": 15
    }
}


def show_categories() -> list:
    print("Here is the list of categories  available: ")
    categories = []
    for category in PRODUCTS.keys():
        categories.append(category)
        print(category.title()) 
    return categories


def get_category_choice(categories:list) -> str:

    while True:
        category_choice = input(
            f"Enter the category name to view products: "
            f"Enter q to quit"
            ).strip().lower()
        
        if not category_choice:
            print("Choice cannot be empty")
            continue
        
        valid_choices = categories + ["q"]
        if category_choice not in valid_choices:
            print("Only valid choices please")
            continue
    
        return category_choice
    

def show_items(category:dict) -> tuple[str,int]:
    
    products = []
    for product, price in category.items():
        products.append(product.lower())
        print(f"{product} - {price}")
    
    while True:
        product_choice = input(
            "Enter the product name you want to buy: "
            "Enter q to quit "
        ).strip().lower()

        if not product_choice:
                print("Choice cannot be empty")
                continue
        
        valid_choices = products + ["q"]
        print(valid_choices)
        print(product_choice)

        if product_choice not in valid_choices:
                print("Only valid product names please")
                continue
        
        break
    
    number_of_items = get_item_choice()

    return product_choice, number_of_items
        

def get_item_choice():
     
    while True:
        qty_str = input(
            "Enter the number of quantities (1-10): "
        ).lower().strip()

        if not qty_str:
            print("Select atleast one quantity to proceed ")
        
        try:
            qty = int(qty_str)
            if qty not in range(1,11):
                print("Minimum 1 Maximum 10")
                continue
        except ValueError:
            print("Only numbers please")

        return qty


def add_to_cart(product_choice:str, qty:int, category:dict) -> int:

    for product, price in category.items():
        if product == product_choice:
            sub_total = int(price * qty)
    
    
    return sub_total


def quit_application():
    while True:
        user_choice = input("" \
                "Enter you choice (Y/N): "
                ).strip().lower()

        if user_choice not in ["y","n"]:
            print("only valid choices: Y/N")
            continue

        return user_choice
    

def main():
    total = 0
    final_list ={}
    while True:
        categories_list = show_categories()
        category_choosen = get_category_choice(categories= categories_list)
        if category_choosen == "q":
            print("Thank you!")
            break

        for category, items in PRODUCTS.items():
            if category == category_choosen:
                category_listings = items
        while True: 
            product_choice, number_of_items  = show_items(category=category_listings)

            if product_choice == "q":
                print("Thank you!")
                break

            sub_total = add_to_cart(
                product_choice=product_choice,
                qty=number_of_items,
                category=category_listings
                )
            print(f"The selected product is {product_choice}")
            print(f"The quantity is {number_of_items}")
            print(f"The subtotal is {sub_total}")
            final_list[product_choice] = {
                "qty":number_of_items,
                "sub_total":sub_total
            }
            print("Y to continue adding more products from the same category")
            print("N to move on to next category")
            user_option = quit_application()
            
            if user_option == "y":
                continue
            else:
                break
        print("Y to continue adding  products from the other categories")
        print("N to quit")
        user_choice = quit_application()
        if user_choice == "y":
            continue
        else:
            break
    
    print("=====================Your Final Bill Summary=====================")
    
    for item_name, details in final_list.items():
        quantity = details["qty"]
        item_total = details["sub_total"]
        total += details["sub_total"]
        print(
            f"Item: {item_name} | "
            f"Quantity: {quantity} | "
            f"Subtotal: {item_total}"
        )

    print(f"Your grand total is {total}")
    
    
if __name__ == "__main__":
    main()


        

    

