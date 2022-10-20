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
        print("Enter Details of customer you wish to add")
        add_customer()
        print("How do ou wish to proceed?")
        customer_menu()
    elif value == 2:
        print("What do you wish to update?")
        update_customer()
        customer_menu()

    elif value == 3:
        print("Delete Customer")
        delete_customer()
        customer_menu()
    elif value == 4:
        # view_all_products()
        from product import product_operations
        product_operations.view_all_products()
    elif value == 5:
        view_all_customers()
        customer_menu()
    elif value == 6:
        from main import main_menu
        main_menu()


customer_menu()