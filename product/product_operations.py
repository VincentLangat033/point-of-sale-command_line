import json
product_json = "product/products.json"


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
        print(f"Index of product: {i}")
        print(f"Name of product: {name}")
        print(f"Cost of product: {cost}")
        print(f"Available quantity of the product: {quantity} pieces")
        print(f"The ID of the product: {id} ")
        print("\n")
        i = i+1


def add_product():
    f = open(product_json, 'r')
    products = json.load(f)

    product = {
        "name": input("Enter Name: "),
        "cost": input("Cost: "),
        "quantity": input("Quantity: "),
        "id": input("ID: ")

    }

    products.append(product)

    with open(product_json, 'w', encoding='utf-8') as json_file:
        json.dump(products, json_file, indent=4, separators=(',', ': '))
        print("Product inserted successfully")
    # print(customers)


def update_product():
    print("Want to update a product?")
    print("Press 1 to view index of product you want to update:")
    # print("Press 2 to exit operation")
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_all_products()
        new_data = []
        f = open(product_json, 'r')
        products = json.load(f)
        data_length = len(products) - 1
        print("Which index would you like to update?")
        edit_option = input(f"Select a number between 0 and {data_length}: ")
        i = 0
        for product in products:
            if i == int(edit_option):
                name = product["name"]
                cost = product["cost"]
                quantity = product["quantity"]
                id = product["id"]
                print(f"Name of product is:  {name}")
                name = input("What would you like the new name of product be?:  ")
                print(f"Age of product is: {cost}")
                cost = input("What would you like the new cost of product be?:  ")
                print(f"Quantity of product is: {quantity}")
                quantity = input("What would you like the new quantity of product be?:  ")
                print(f"ID of product is: {id}")
                id = input("What would you like the new ID of product be?:  ")
                new_data.append({"name": name, "cost": cost, "quantity": quantity, "id": id})
                print("\n")

                i = i + 1
            else:
                new_data.append(product)
                i = i + 1
        with open(product_json, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print("Customer updated successfully")

    else:
        print("Invalid input try again")
        update_product()


def delete_product():
    print("Want to delete a Product?")
    print("Press 1 to view index of Product you want to delete:")
    # print("Press 2 to exit operation")
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_all_products()
        new_data = []
        f = open(product_json, 'r')
        products = json.load(f)
        data_length = len(products)-1
        print("Which index would you like to delete?")
        delete_option = input(f"Select a number between 0 and {data_length}: ")
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
            print("Product deleted successfully")

    else:
        print("Invalid input try again")
        delete_product()





