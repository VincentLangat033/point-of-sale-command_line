from customer.customer_menu import customer_menu


def main_menu():
    print("""
----------------------------------

*** Welcome to Python PoS CLI  ***

----------------------------------
    """)
    print("1. Customer Operations ")
    print("2. Product Operations ")
    print("3. Purchase Operations")
    print("""
    """)
    value = int(input("Enter operation you wish to perform : "))
    if value == 1:
        print("""
---------------------------------------------
    ***   Proceed to Customer Operations ***
---------------------------------------------
        """)
        customer_menu()


    elif value == 2:
        product_menu()
    elif value == 3:
        purchase_menu()
    else:
        print("Try again")
        main_menu()


main_menu()
