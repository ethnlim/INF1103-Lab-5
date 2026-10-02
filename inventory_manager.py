def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
    except ValueError:
        print("Invalid price or stock quantity. Product not added.\n")
        return

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    print("Product added successfully!\n")


def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()

    product = search_by_id(inventory, product_id)
    if product is None:
        print("Product not found.\n")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    try:
        new_stock = int(input("New Stock Quantity: ").strip())
    except ValueError:
        print("Invalid quantity. Stock not updated.\n")
        return

    product["stock"] = new_stock
    print("Stock updated successfully!\n")


def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    product = search_by_id(inventory, product_id)
    if product is None:
        print("Product not found.\n")
        return

    print("Product Found")
    print("-" * 50)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 50)


def search_by_id(inventory, product_id):
    """Helper: returns the matching product dict, or None."""
    for product in inventory:
        if product["id"] == product_id:
            return product
    return None


def display_all(inventory):
    print("Current Inventory")
    print("-" * 50)
    if not inventory:
        print("Inventory is empty.")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 50)


def print_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = [
        {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
    ]

    while True:
        print_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            print("(Haven't implemented save function yet)\n")
        elif choice == "6":
            print("Exiting (Haven't implemented save function yet).")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()