# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_categories():
    """Displays available categories."""
    print("Available categories:")
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    try:
        category_choice = int(input("Please select a category by number: ")) - 1
        return category_choice
    except ValueError:
        return None


def display_products(products_list):
    """Displays products in the chosen category."""
    print("Available products:")
    for index, (product_name, product_price) in enumerate(products_list, start=1):
        print(f"{index}. {product_name} - ${product_price:.2f}")


def display_sorted_products(products_list, sort_order):
    """Sorts and returns products based on the sort order."""
    if sort_order == "asc":
        sorted_products = sorted(products_list, key=lambda x: x[1])  
    else:
        sorted_products = sorted(products_list, key=lambda x: x[1], reverse=True)  
    return sorted_products


def add_to_cart(cart, product, quantity):
    """Adds a product to the cart."""
    cart.append((product[0], product[1], quantity))  


def display_cart(cart):
    """Displays the items in the cart and returns the total cost."""
    total_cost = 0
    for product, price, quantity in cart:
        product_total = price * quantity
        total_cost += product_total
        print(f"{product} - ${price} x {quantity} = ${product_total}")
    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    """Generates and displays a receipt."""
    print(f"\nCustomer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")


def validate_name(name):
    """Validates that the name contains first and last names, and is alphabetic."""
    if len(name.split()) == 2 and all(part.isalpha() for part in name.split()):
        return True
    return False


def validate_email(email):
    """Validates that the email contains '@'."""
    return "@" in email


def main():
    """Main shopping function."""
    pass  # Placeholder for the main function that will be used in testing
