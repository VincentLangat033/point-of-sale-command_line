
def product_menu():
    print("What would you like to do?")
    print("1. View all products")
    print("2. Insert a new product")
    print("3. Update a Product")
    print("4. Delete a Product")
    print("5. Proceed to make a purchase")
    print("5. Quit")
    value = input("Enter a number to proceed: ")
    if value == "1":
        from product import product_operations
        product_operations.view_all_products()
        product_menu()
    elif value == "2":
        from product import product_operations
        product_operations.add_product()
        product_menu()
    elif value == "3":
        from product import product_operations
        product_operations.update_product()
        product_menu()
    elif value == "4":
        from product import product_operations
        product_operations.delete_product()
        product_menu()

    else:
        print("Invalid number, try again!")