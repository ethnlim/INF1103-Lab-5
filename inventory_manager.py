import json
import os

INVENTORY_FILE = "inventory.json"


def load_inventory(filename=INVENTORY_FILE):
    """Load inventory list from disk. Returns a list of product dicts."""
    if not os.path.exists(filename):
        print(f"{filename} not found. Starting with empty inventory.")
        return []
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            print(f"{filename} found.")
            print("Inventory loaded successfully.")
            return data
    except (json.JSONDecodeError, ValueError):
        print(f"{filename} is corrupted or empty. Starting with empty inventory.")
        return []

def save_inventory(inventory, filename=INVENTORY_FILE):
    """Save the inventory list to disk as JSON."""
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)

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

    inventory = load_inventory()

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
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.\n")
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()