import json
from termcolor import colored
import os
import smtplib

filename = "/home/moringa/PycharmProjects/SEPA/sprint_one/customer/customers.json"
product_file = "/home/moringa/PycharmProjects/SEPA/sprint_one/product/products.json"
cart_file = "/home/moringa/PycharmProjects/SEPA/sprint_one/purchases/cart.json"


def user_json_file():
    """

    This action opens the customers json file and return its data

    """
    with open(filename) as file:
        data = json.load(file)
    return data


def product_json_file():
    """
    This action opens the products json file and return its data

    """
    with open(product_file) as file:
        data = json.load(file)
    return data


def check_user(customer):
    """
    Action to Check if a Customer exists
    """
    users = user_json_file()
    # print(users)
    for (index, entry) in enumerate(users):
        if customer == entry["id"]:
            return str(index)
        else:
            # print(colored("Wrong customer ID", "red"))
            # print(colored("Try again!", "red"))
            continue
    return False


def check_product(product):
    """
    Action to check if a product truly exists
    """
    users = product_json_file()
    # print(users)
    for (product_index, entry) in enumerate(users):
        if product == entry["id"]:
            return str(product_index)
        else:
            print(colored("Wrong product ID", "red"))
            print(colored("Try again!", "red"))
            continue
            # purchase_menu()
    return False


def goods_bought(quantity, cost, email):
    """
    Goods bought by the customer will be appended to the database
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
    Stores the goods that a customer has bought, minuses products purchases
    """
    updated_product_list = []
    product_details = product_json_file()
    for product in product_details:
        if name == product["name"]:
            name = product["name"]
            quantity = int(product["quantity"]) - int(goods_sold)
            cost = product["cost"]
            id = product["id"]
            updated_product = {
                "name": name,
                "quantity": quantity,
                "cost": cost,
                "id": id,
            }
            updated_product_list.append(updated_product)
        else:
            updated_product_list.append(product)
    with open(product_file, "w") as f:
        json.dump(updated_product_list, f, indent=4)


def send_email(email_receiver, subject, text):
    """
     email_receiver:
    :param subject:
    :param text:
    :return:
    # wdfjlrrmhebayvts - authenitcation token to be used in place of email address
       # subject = "hello there"
    # text = "Good morning"
    # email_receiver = "kimutaiketer033@gmail.com"
    """
    email = "vlangat439@gmail.com"
    password = "qaytwectapjlgdik"
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
    print(colored("Email Sent Successfully!", "yellow"))


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
                    customer_id = int(input(colored(f"\nEnter Customer ID(1-{data_length}) of the buyer: >> ", "blue")))
                except ValueError:
                    print(colored(f"\nINVALID INPUT!", "red"))
                    continue
                if customer_id > data_length:
                    print(colored("CUSTOMER DOES NOT EXIST! Enter VALID Customer ID!", "red"))
                    continue
                else:
                    break
            i = 1
            for entry in customer_temp:
                if i == int(customer_id):
                    final_order["Customer Name"] = entry["name"]
                    customer_mail = entry["email"]
                    customer_name = entry["name"]
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
                print(colored("""
`````````````````````````````````
   MAKE YOUR PURCHASES HERE:
   
`````````````````````````````````
                """, "blue"))
                buyer_choice = input(colored("Which laptop ID do you want?\n", "blue"))
                pairs = input(colored("How many pieces do you need?\n", "blue"))
                cart = [product[int(buyer_choice)]["name"], int(pairs), product[int(buyer_choice)]["cost"],
                        int(pairs) * int(product[int(buyer_choice)]["cost"])]
                main_cart.append(cart)
                print(main_cart)
                print(colored("""
```````````````````````````````
ENJOYED YOUR SHOPPING?
  - YOU HAVE ALL YOU NEED? (can never be enough though 😊)
  
```````````````````````````````                
                """, "blue"))
                print(colored("Do you want to continue shopping? ", "blue"))
                print(colored("Enter yes to continue shopping: ", "blue"))
                print(colored("Enter no to proceed to check-out: ", "blue"))
                user_choice = input(colored("Your choice here: ", "blue"))
                if user_choice.lower() == "yes":
                    continue
                elif user_choice.lower() == "no":
                    # user_id = input("Enter a value")

                    break
                else:
                    print(colored("Please choose valid answer.", "red"))
            total_cost = 0
            # print(entry["email"])
            index = check_user(customer)
            # print(index)
            for i in main_cart:
                total_cost += i[3]
            goods_sold(cart[0], cart[1])
            goods_bought(cart[1], total_cost, customer[int(index)]["email"])
            purchase_details = ''.join([f"""
{i[0]}     -       {i[1]}   :   {i[2]}  @    :    {i[2]  * i[1]}   \n
    """ for i in main_cart])

            receipt = colored(f"""
````````````````````````````````````````````````````````````````````
THANK YOU {customer_name} FOR SHOPPING WITH US

                CUSTOMER RECEIPT
`````````````````````````````````````````````````````````````````````
    Customer name: {customer_name}

`````````````````````````````````````````````````````````````````````
    Product         Quantity           Price       Sub-Total
`````````````````````````````````````````````````````````````````````
    {purchase_details}    
    
        
    Total purchase cost  : {total_cost}
    
YOU WERE SERVED BY: VINCENT KIMUTAI
    
``````````````````````````````````````````````````````````````````````
            """, "yellow")

            print(receipt)
            print(colored("""
            Thank you for purchasing with us!
            Do you want a receipt for this transaction sent to your email?
            Press 1 if you accept and any other value to exit.
            """, "yellow"))
            user_id = input(colored("Enter a value: ", "blue"))
            if user_id == "1":
                send_email(customer_mail, " Here is your POS CLI receipt", receipt)
            else:
                pass
            user_input = input(colored("Type exit to exit or 1 to go back home: ", "yellow"))
            if user_input == "exit":
                pass
            elif user_input == "1":
                from main import main_menu
                main_menu()
            else:
                pass


def product_purchase(final_order):
    from product import product_operations
    product_operations.view_all_products()

    with open(product_file, "r") as json_file:
        product_temp = json.load(json_file)
    data_length = len(product_temp)

    with open(cart_file, "r") as json_file:
        cart_temp = json.load(json_file)
    option = int(
        input(colored(f"Enter Product ID between (1 - {data_length}) of item you wish to add to cart: >> ", "blue")))
    i = 1
    for entry in product_temp:

        if i == int(option):
            product_detail = create_product_id()
            final_order[product_detail] = {}
            prod_qty = entry["quantity"]
            # print(prod_qty)
            final_order[product_detail]["id"] = option
            final_order[product_detail]["name"] = entry["name"]
            final_order[product_detail]["quantity"] = int(input(colored(f"\nEnter quantity (less than or equal "
                                                                 f"to {prod_qty}) you wish to purchase: >> ", "blue")))
            final_order[product_detail]["Product_Price"] = entry["cost"]
            price = float(final_order[product_detail]["Product_Price"])
            subtotal = price * final_order[product_detail]["quantity"]
            final_order[product_detail]["Sub-Total"] = float(subtotal)
            print(subtotal)
            cart_temp.append(final_order)
            i = i + 1

        else:
            pass
            i = i + 1
    with open(cart_file, "w") as json_file:
        json.dump(cart_temp, json_file, indent=4)
        print(colored("\n\n*****Product Added to cart!*****", "blue"))

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


# make_purchases()
# process_purchase()

# purchase_menu()

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
# make_purchases()