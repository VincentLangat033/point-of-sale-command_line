from product_operations import view_all_products
import json
import os
filename = "customers.json"
product_file = "products.json"


# def check_if_user_id_exist():
#     # with open(filename) as file:  # opens json file
#     #     data = json.load(file)  # loads the data
#     f = open('customers.json', 'r')
#     customers = json.load(f)
#     for customer in customers:
#         name = customer["name"]
#
#     # f = open('customers.json', 'r')
#     # customers = json.load(f)
#
#     # print(customers)
#
#         print(name)
#         print(customer)
#         user_id = input("Verify your Customer ID: ")
#         if (customer.get('id')) == user_id:
#             print("Your ID exists lets proceed")
#             print("Enter 1 to view a list of products so you can purchase")
#             # purchase_menu()
#             # user_id = user_id
#
#             break
#         else:
#             print("Your ID does not exist. Wanna create a new customer?")
#             print("Enter 1 to create a new customer: ")
#             print("Enter 2 to try again: ")
#             user_input = int(input("Enter option: "))
#             if user_input == "1":
#                 add_customer()
#             elif user_input == "2":
#
#                 check_if_user_id_exist()
#
#             else:
#                 print("You entered an invalid option!")
#                 check_if_user_id_exist()
#
#             break


def user_json_file():
    """
    Opens the json file and reads its content
    """
    with open(filename) as file:  # opens json file
        data = json.load(file)  # loads the data
    return data


def product_json_file():
    """
    Opens the json file and reads its content
    """
    with open(product_file) as file:  # opens json file
        data = json.load(file)  # loads the data

    return data

# def check_if_user_valid():
#     """
#     Checks if a user exist or not.
#     """
#     users = user_json_file()
#     customer = input("enter id: ")
#     # print(users)
#     for (index, entry) in enumerate(users):
#         if customer == entry["id"]:
#
#             # print(index)
#             # start_purchases()
#             purchase_menu()
#
#             return str(index)
#         else:
#             # print("not success")
#             continue
#     return False


def check_user(customer):
    """
    Checks if a user exist or not.
    """
    users = user_json_file()
    # print(users)
    for (index, entry) in enumerate(users):
        if customer == entry["id"]:  # remember to use users input
            return str(index)
        else:
            print("Wrong customer ID")
            print("Try again!")
            continue
            # purchase_menu()

    return False


def check_product(product):
    """
    Checks if a product exist or not.
    """
    users = product_json_file()
    # print(users)
    for (product_index, entry) in enumerate(users):
        if product == entry["id"]:  # remember to use users input
            return str(product_index)
        else:
            print("Wrong product ID")
            print("Try again!")
            continue
            # purchase_menu()

    return False


def purchase_menu():
    customers = user_json_file()
    products = product_json_file()
    print("""
    **  Welcome to purchases  ***
    *** Lets Proceed ***
    """)
    print("Enter your Customer ID so you can proceed to purchases")
    customer = input("Please enter your ID: \n")
    index = check_user(customer)
    main_cart = {}
    if check_user(customer):
        while True:
            print("Here is the list of products available")
            view_all_products()
            product = input("Please enter the product ID")
            product_index = check_product(product)
            if check_product(product):
                print("Lets proceed")
                product_to_buy = fetch_product_by_id(product_index, product_index).get("product_name")
                print(product_to_buy)
            break


# def fetch_product_by_index(product_index):
#     f = open('products.json', 'r')
#     products = json.load(f)
#     i = 0
#
#     for product in products:
#         # name = product["name"]
#         # cost = product["cost"]
#         # quantity = product["quantity"]
#         # id = product["id"]
#         # print(product["id"])
#         print(product)
#         # return product


def fetch_product_by_id(cls, id):
    product = []
    file = open('products.json', 'r')
    if os.stat('products.json').st_size == 0:
        product = []
    else:
        products = json.load(file)
        for each in products:
            if each.get("id") == id:
                product = each
    return product






purchase_menu()