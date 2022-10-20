from termcolor import colored


def product_menu():
    print(colored("""
***  YOU ARE AT THE PRODUCT'S SECTION   ***
    WHAT WOULD YOU LIKE TO DO?
    1. View all products
    2. Insert a new product
    3. Update a Product
    4. Delete a Product
    5. Proceed to make a purchase
    6. Quit
        
    
    """, "blue"))
    value = input(colored("Enter a number to proceed: ", "blue"))
    if value == "1":
        from product import product_operations
        product_operations.view_all_products()
        value = input(colored("Press 1 to get back to product menu: ", "yellow"))
        if value == "1":
            product_menu()
        else:
            pass
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


product_menu()
