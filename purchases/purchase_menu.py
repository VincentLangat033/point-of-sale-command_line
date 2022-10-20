import json
import os
import smtplib
filename = "/home/moringa/PycharmProjects/SEPA/sprint_one/customer/customers.json"
product_file = "/home/moringa/PycharmProjects/SEPA/sprint_one/product/products.json"
cart_file = "/home/moringa/PycharmProjects/SEPA/sprint_one/purchases/cart.json"


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


def goods_bought(quantity, cost, email):
    """
    Inputs the goods that the user has bought in the db.
    """
    updated_user_list = []
    user_details = user_json_file()
    for user in user_details:
        if email == user["email"]:
            name = user["name"]
            email = user["email"]
            phone = user["phone"]
            age = user["age"]
            id = user["id"]
            # user['products'] = int(user["products"]) + int(quantity)
            # user['expenditure'] = int(user['expenditure']) + int(cost)
            updated_user = {
                "name": name,
                "email": email,
                "phone": phone,
                "age": age,
                "id": id
                # "products": user["products"],
                # "expenditure": user["expenditure"]
            }
            updated_user_list.append(updated_user)
        else:
            updated_user_list.append(user)
    with open(filename, "w") as f:
        json.dump(updated_user_list, f, indent=4)


def create_product_id():
    with open(cart_file, "r") as json_file:
        gen_temp = json.load(json_file)
    if not gen_temp:
        new_id = 1
        return new_id
    else:
        [open_gen_temp] = gen_temp
        prev_id = list(open_gen_temp)[-1]
        length = len(prev_id)
        num = int(length) + 1
        new_id = num
        return new_id


def goods_sold(name, goods_sold):
    """
    Inputs the goods that the user has bought in the db.
    """
    updated_product_list = []
    product_details = product_json_file()
    for product in product_details:
        if name == product["name"]:
            name = product["name"]
            quantity = int(product["quantity"]) - int(goods_sold)
            cost = product["cost"]

            updated_product = {
                "name": name,
                "quantity": quantity,
                "cost": cost,
            }
            updated_product_list.append(updated_product)
        else:
            updated_product_list.append(product)
    with open(product_file, "w") as f:
        json.dump(updated_product_list, f, indent=4)


def send_email(email_receiver, subject, text):
    # wdfjlrrmhebayvts


    email = "vlangat439@gmail.com"
    password = "wdfjlrrmhebayvts"
    # subject = "hello there"
    # text = "Good morning"
    # email_receiver = "kimutaiketer033@gmail.com"
    sender_email = email
    receiver_email = email_receiver
    password = password

    subject = subject
    text = text

    message = 'Subject: {}\n\n{}'.format(subject, text)

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message, subject)
    print("Email Sent Successfully!")

def make_purchases():
    final_order = {}
    with open(cart_file, "r") as json_file:
        order_temp = json.load(json_file)
    # checks if cart is empty
    if not order_temp:
        from customer import customer_operations
        customer_operations.view_all_customers()
        with open(filename, "r") as json_file:
            customer_temp = json.load(json_file)
            data_length = len(customer_temp)
            while True:
                try:
                    customer_id = int(input(f"\nEnter Customer ID(1-{data_length}) of the buyer: >> "))
                except ValueError:
                    print(f"\nINVALID INPUT!")
                    continue
                if customer_id > data_length:
                    print("CUSTOMER DOES NOT EXIST! Enter VALID Customer ID!")
                    continue
                else:
                    break

            i = 1
            for entry in customer_temp:
                if i == int(customer_id):
                    final_order["Customer Name"] = entry["name"]
                    customer_mail = entry["email"]
                    print(customer_mail)

                    order_temp.append(final_order)
                    i = i + 1
                else:
                    pass
                    i = i + 1
            main_cart = []

            while True:
                product = product_json_file()
                customer = user_json_file()

                buyer_choice = input("Which laptop ID do you want?\n")
                pairs = input("How many pieces do you need?\n")
                cart = [product[int(buyer_choice)]["name"], int(pairs), product[int(buyer_choice)]["cost"],
                        int(pairs) * int(product[int(buyer_choice)]["cost"])]
                main_cart.append(cart)
                print(main_cart)

                print("Do you want to continue shopping? ")
                print("* yes ")
                print("* no ")
                user_choice = input("")
                if user_choice.lower() == "yes":
                    continue
                elif user_choice.lower() == "no":
                    # user_id = input("Enter a value")

                    break
                else:
                    print("Please choose valid answer.")
            total_cost = 0
            # print(entry["email"])
            index = check_user(customer)
            # print(index)
            for i in main_cart:
                total_cost += i[3]
            goods_sold(cart[0], cart[1])
            goods_bought(cart[1], total_cost, customer[int(index)]["email"])
            the_join = ''.join([f"{i[0]}  -  {i[1]}  : {i[2]}  each\n" for i in main_cart])

            receipt = f"""
    Customer Receipt
    _________________________________________________
    Customer name: {customer[int(index)]["name"]}
    _________________________________________________
    Product   Quantity     price   
    _________________________________________________   
    {the_join}         
    Total purchase cost  : {total_cost}
    _________________________________________________   
            """

            print(receipt)
            user_id = input("Enter a value")
            if user_id == "1":
                send_email(customer_mail, " Here is your POS CLI receipt", receipt)



def product_purchase(final_order):
    from product import product_operations
    product_operations.view_all_products()

    with open(product_file, "r") as json_file:
        product_temp = json.load(json_file)
    data_length = len(product_temp)

    with open(cart_file, "r") as json_file:
        cart_temp = json.load(json_file)
    option = int(input(f"Enter Product ID(1 - {data_length}) of item you wish to add to cart: >> "))
    i = 1
    for entry in product_temp:

        if i == int(option):
            prod_id = create_product_id()
            final_order[prod_id] = {}
            prod_qty = entry["quantity"]
            # print(prod_qty)
            final_order[prod_id]["id"] = option
            final_order[prod_id]["name"] = entry["name"]
            final_order[prod_id]["quantity"] = int(input(f"\nEnter quantity (less than or equal "
                                                      f"to {prod_qty}) you wish to purchase: >> "))
            final_order[prod_id]["Product_Price"] = entry["cost"]
            price = float(final_order[prod_id]["Product_Price"])
            subtotal = price * final_order[prod_id]["quantity"]
            final_order[prod_id]["Sub-Total"] = float(subtotal)
            print(subtotal)
            cart_temp.append(final_order)
            i = i + 1

        else:
            pass
            i = i + 1
    with open(cart_file, "w") as json_file:
        json.dump(cart_temp, json_file, indent=4)
        print("\n\n*****Product Added to cart!*****")




# make_purchases()
# process_purchase()

# purchase_menu()