import json


def add_customer():
    f = open('customers.json', 'r')
    customers = json.load(f)

    customer = {
        "name": input("Enter Name: "),
        "age": int(input("Age: ")),
        "id": int(input("Customer ID: "))

    }

    customers.append(customer)

    with open('customers.json', 'w', encoding='utf-8') as json_file:
        json.dump(customers, json_file, indent=4, separators=(',', ': '))
        print("Customer created successfully")
    print(customers)


def view_all_customers():
    # with open('test.json') as f:
    #     data = json.loads(f)
    #     print(data)
    f = open('customers.json', 'r')
    customers = json.load(f)
    i = 0

    for customer in customers:
        name = customer["name"]
        age = customer["age"]
        id = customer["id"]
        print(f"Index of customer {i}")
        print(f"Name of customer {name}")
        print(f"Age of customer {age}")
        print(f"ID of customer {id}")
        print("\n")
        i = i+1



def delete_customer():
    print("Want to delete a customer?")
    print("Press 1 to view index of Customer you want to delete:")
    # print("Press 2 to exit operation")
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_all_customers()
        new_data = []
        f = open('customers.json', 'r')
        customers = json.load(f)
        data_length = len(customers)-1
        print("Which index would you like to delete?")
        delete_option = input(f"Select a number between 0 and {data_length}: ")
        i = 0
        for customer in customers:
            if i == int(delete_option):
                pass
                i = i + 1
            else:
                new_data.append(customer)
                i = i + 1
        with open('customers.json', 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print("Customer deleted successfully")

    else:
        print("Invalid input try again")
        delete_customer()


def update_customer():
    print("Want to update a customer?")
    print("Press 1 to view index of Customer you want to update:")
    # print("Press 2 to exit operation")
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_all_customers()
        new_data = []
        f = open('customers.json', 'r')
        customers = json.load(f)
        data_length = len(customers) - 1
        print("Which index would you like to update?")
        edit_option = input(f"Select a number between 0 and {data_length}: ")
        i = 0
        for customer in customers:
            if i == int(edit_option):
                name = customer["name"]
                age = customer["age"]
                id = customer["id"]
                print(f"Name of customer is:  {name}")
                name = input("What would you like the new name of customer be?:  ")
                print(f"Age of customer is: {age}")
                age = int(input("What would you like the new age of customer be?:  "))
                print(f"ID of customer is: {id}")
                id = int(input("What would you like the new id of customer be?:  "))
                new_data.append({"name": name, "age": age, "id": id})
                print("\n")

                i = i + 1
            else:
                new_data.append(customer)
                i = i + 1
        with open('customers.json', 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print("Customer updated successfully")

    else:
        print("Invalid input try again")
        update_customer()



