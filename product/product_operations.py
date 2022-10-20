import json
from termcolor import colored
product_json = "/home/moringa/PycharmProjects/SEPA/sprint_one/product/products.json"


def view_all_products():
    # with open('test.json') as f:
    #     data = json.loads(f)
    #     print(data)
    f = open(product_json, 'r')
    products = json.load(f)
    i = 0
    for product in products:
        name = product["name"]
        cost = product["cost"]
        quantity = product["quantity"]
        id = product["id"]
        print(colored(f"Index of product : {i}", "yellow"))
        print(colored(f"Name of product : {name}", "blue"))
        print(colored(f"Cost of product : {cost}", "blue"))
        print(colored(f"Available quantity of the product : {quantity} pieces", "yellow"))
        print(colored(f"The ID of the product : {id} ", "blue"))
        print(colored("""
______________________________________________
""", "blue"))
        i = i+1


def add_product():
    f = open(product_json, 'r')
    products = json.load(f)
    print(colored("""
`````````````````````````````````````
    ADD PRODUCT SECTION: 
      - ADD YOUR PRODUCT HERE
`````````````````````````````````````
""", "blue"))
    product = {
        "name": input(colored("Enter Name: ", "blue")),
        "cost": input(colored("Cost: ", "blue")),
        "quantity": input(colored("Quantity: ", "blue")),
        "id": input(colored("ID: ", "blue"))

    }
    products.append(product)
    with open(product_json, 'w', encoding='utf-8') as json_file:
        json.dump(products, json_file, indent=4, separators=(',', ': '))
        print(colored("Product inserted successfully", "yellow"))
    # print(customers)


def update_product():
    print(colored("""
    `````````````````````````````````````
        UPDATE PRODUCT SECTION: 
         - UPDATE YOUR PRODUCT HERE
    `````````````````````````````````````
    """, "blue"))
    print(colored("Press 1 to view products by index", "yellow"))
    user_input = input(colored("Enter value to proceed: ", "blue"))
    if user_input == "1":
        view_all_products()
        new_data = []
        f = open(product_json, 'r')
        products = json.load(f)
        data_length = len(products) - 1
        print(colored("Which index would you like to update?", "yellow"))
        edit_option = input(colored(f"Select a number between 0 and {data_length}: ", "blue"))
        i = 0
        for product in products:
            if i == int(edit_option):
                name = product["name"]
                cost = product["cost"]
                quantity = product["quantity"]
                id = product["id"]
                print(colored(f"Name of product is:  {name}", "yellow"))
                name = input(colored("What would you like the new name of product be?:  ", "blue"))
                print(colored(f"Age of product is: {cost}", "yellow"))
                cost = input(colored("What would you like the new cost of product be?:  ", "blue"))
                print(colored(f"Quantity of product is: {quantity}", "yellow"))
                quantity = input(colored("What would you like the new quantity of product be?:  ", "blue"))
                print(colored(f"ID of product is: {id}", "yellow"))
                id = input(colored("What would you like the new ID of product be?:  ", "blue"))
                new_data.append({"name": name, "cost": cost, "quantity": quantity, "id": id})
                print("\n")
                i = i + 1
            else:
                new_data.append(product)
                i = i + 1
        with open(product_json, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print(colored("Product updated successfully", "yellow"))
    else:
        print(colored("Invalid input try again", "red"))
        update_product()


def delete_product():
    print(colored("""
    `````````````````````````````````````
        DELETE PRODUCT SECTION: 
         - DELETE YOUR PRODUCT HERE
         
    `````````````````````````````````````
    """, "blue"))
    print(colored("Press 1 to view the index of the Product you want to delete: ", "yellow"))
    user_input = input(colored("Enter value to proceed: ", "blue"))
    if user_input == "1":
        view_all_products()
        new_data = []
        f = open(product_json, 'r')
        products = json.load(f)
        data_length = len(products)-1
        print(colored("Which index would you like to delete?", "yellow"))
        delete_option = input(colored(f"Select a number between 0 and {data_length}: ", "blue"))
        i = 0
        for product in products:
            if i == int(delete_option):
                pass
                i = i + 1
            else:
                new_data.append(product)
                i = i + 1
        with open(product_json, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print(colored("Product deleted successfully!", "yellow"))
    else:
        print(colored("Invalid input try again!", "red"))
        delete_product()



# view_all_products()
# add_product()
# delete_product()

