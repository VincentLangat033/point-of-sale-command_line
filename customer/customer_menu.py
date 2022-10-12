
def customer_menu():
    print("What would you like to do?")
    print("1. Add a customer")
    print("2. Update a customer")
    print("3. Delete a Customer")
    print("4. Check available products")
    print("5. View all customers")
    print("6. Go Back Home")
    print("7. Quit")
    print("""
    """)

    value = int(input("Enter action you would like to do : "))

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
        view_all_products()
        print("What do you wish to do? ")
    elif value == 5:
        view_all_customers()
    elif value == 6:
        main_menu()