from termcolor import colored
from customer.customer_operations import add_customer, view_all_customers, delete_customer, update_customer


def customer_menu():
    print(colored("""
  What would you like to do?

````````````````````````````````````````````````
    1. Add a customer
    2. Update a customer
    3. Delete a Customer
    4. Check available products
    5. View all customers
    6. Go Back Home
    7. Quit
    
```````````````````````````````````````````````````
    """, "blue"))
    value = int(input(colored("Enter action you would like to do :\n", "yellow")))
    print("""
    
    """)
    if value == 1:
        print(colored("Enter Details of customer you wish to add", "yellow"))
        add_customer()
        print(colored("How do ou wish to proceed?",  "yellow"))
        customer_menu()
    elif value == 2:
        print(colored("What do you wish to update?", "yellow"))
        update_customer()
        customer_menu()

    elif value == 3:
        print(colored("Delete Customer", "yellow"))
        delete_customer()
        customer_menu()
    elif value == 4:
        from product import product_operations, product_menu
        product_operations.view_all_products()
        user_input = input(colored("Press 1 to proceed to product menu", "yellow"))
        if user_input == "1":
            product_menu.product_menu()
        else:
            product_menu.product_menu()

    elif value == 5:
        view_all_customers()
        user_input = input(colored("Enter 1 to return to Customer Menu or 0 to quit at this point: ", "yellow"))
        if user_input == "1":
            customer_menu()
        elif user_input == "0":
            pass
        else:
            print(colored("Input Invalid!, Try again!", "red"))
    elif value == 6:
        from main import main_menu
        main_menu()


# customer_menu()
