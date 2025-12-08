
PRODUCTS: dict[str, dict[str, int]] = {
    "tops": {
        "t-shirt": 30,
        "shirt": 50,
        "hoodie": 60,
        "sweater": 55,
    },
    "bottoms": {
        "shorts": 20,
        "pants": 50,
        "jeans": 70,
        "joggers": 40,
    },
    "footwear": {
        "sneakers": 80,
        "sandals": 35,
        "boots": 120,
    },
    "accessories": {
        "cap": 10,
        "belt": 25,
        "socks": 5,
        "scarf": 15,
    },
}


def show_categories() -> list[str]:
    """Display all categories and return them as a list."""
    print("\nAvailable Categories:")
    categories = list(PRODUCTS.keys())
    for cat in categories:
        print(f"- {cat.title()}")
    return categories


def get_category_choice(categories: list[str]) -> str:
    """Ask user to choose a category or quit."""
    while True:
        choice = input("\nEnter category name (or 'q' to quit): ").strip().lower()
        
        if not choice:
            print("Choice cannot be empty.")
            continue
        
        if choice in categories or choice == "q":
            return choice
        
        print("Invalid choice. Try again.")


def show_items(items: dict[str, int]) -> tuple[str, int]:
    """Show items inside selected category and return chosen item + quantity."""
    
    print("\nProducts:")
    available_products = list(items.keys())
    for product, price in items.items():
        print(f"- {product.title()} : ${price}")

    while True:
        product_choice = input("Enter product name (or 'q' to quit): ").strip().lower()

        if not product_choice:
            print("Choice cannot be empty.")
            continue

        if product_choice in available_products or product_choice == "q":
            break

        print("Invalid product. Try again.")

    if product_choice == "q":
        return "q", 0

    qty = get_item_quantity()
    return product_choice, qty


def get_item_quantity() -> int:
    """Ask user for quantity between 1–10."""
    while True:
        qty_str = input("Enter quantity (1-10): ").strip()

        if not qty_str:
            print("Please enter a number.")
            continue

        try:
            qty = int(qty_str)
            if 1 <= qty <= 10:
                return qty
            print("Quantity must be between 1 and 10.")
        except ValueError:
            print("Only numbers allowed.")


def add_to_cart(product: str, qty: int, items: dict[str, int]) -> int:
    """Return subtotal for selected item."""
    price = items[product]
    return price * qty


def ask_yes_no(prompt: str) -> bool:
    """Ask a Yes/No question. Return True for Yes."""
    while True:
        choice = input(f"{prompt} (Y/N): ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("Only enter Y or N.")


def main() -> None:
    total = 0
    final_list: dict[str, dict[str, int]] = {}

    while True:
        categories = show_categories()
        selected_category = get_category_choice(categories)

        if selected_category == "q":
            print("Thank you!")
            break

        items = PRODUCTS[selected_category]  # simpler

        while True:
            product_choice, qty = show_items(items)

            if product_choice == "q":
                break

            sub_total = add_to_cart(product_choice, qty, items)

            print(f"\nAdded to cart: {product_choice} | Qty: {qty} | Subtotal: {sub_total}")

            final_list[product_choice] = {"qty": qty, "sub_total": sub_total}

            if not ask_yes_no("Add more from this category?"):
                break

        if not ask_yes_no("Do you want to shop another category?"):
            break

    print("\n===================== FINAL BILL =====================")
    for item, details in final_list.items():
        print(f"{item.title():12} | Qty: {details['qty']} | Subtotal: ${details['sub_total']}")
        total += details["sub_total"]

    print(f"\nGrand Total: ${total}")
    print("======================================================")



if __name__ == "__main__":
    main()
