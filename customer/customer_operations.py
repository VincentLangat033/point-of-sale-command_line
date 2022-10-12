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




