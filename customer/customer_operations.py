import json
import re
# from validate_email import validate_email
file_path = "/home/moringa/PycharmProjects/SEPA/sprint_one/customer/customers.json"


def solve(email):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, email):
        return True
    return False


def validate_phone(phone):
    pattern = r"^[07]|[01][0-9]{10}$"
    if re.match(pattern, phone):
        return True
    return False
    # pattern = re.compile("(0|91)?[6-9][0-9]{9}")
    # return pattern.match(phone)


def add_customer():
    f = open(file_path, 'r')
    customers = json.load(f)
    customer = {"name": input("Enter Name: "), "age": int(input("Age: ")), "id": input("Customer ID: ")}
    while True:
        email = input("Customer Email: ")
        if solve(email):
            customer["email"] = email
            break
        else:
            print("Enter the correct email format!")
            continue
    while True:
        phone = input("Enter Phone Number: ")
        if validate_phone(phone):
            customer["phone"] = phone
            break
        else:
            print("Phone number should start with 0 !")
            continue
    customers.append(customer)

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(customers, json_file, indent=4, separators=(',', ': '))
        print("Customer created successfully")
    print(customers)


def view_all_customers():
    # with open('test.json') as f:
    #     data = json.loads(f)
    #     print(data)
    f = open(file_path, 'r')
    customers = json.load(f)
    i = 0

    for customer in customers:
        name = customer["name"]
        age = customer["age"]
        id = customer["id"]
        email = customer["email"]
        phone = customer["phone"]
        print(f"Index of customer {i}")
        print(f"Name of customer {name}")
        print(f"Age of customer {age}")
        print(f"Email of customer {email}")
        print(f"Phone number of customer {phone}")
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
        f = open(file_path, 'r')
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
        with open(file_path, 'w', encoding='utf-8') as json_file:
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
        f = open(file_path, 'r')
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
                phone = customer["phone"]
                email = customer["email"]
                print(f"Name of customer is:  {name}")
                name = input("What would you like the new name of customer be?:  ")
                print(f"Age of customer is: {age}")
                age = int(input("What would you like the new age of customer be?:  "))
                print(f"ID of customer is: {id}")
                age = input("What would you like the new ID of customer be?:  ")
                print(f"Phone No of customer is: {phone}")
                phone = input("What would you like the new Phone No of customer be?:  ")
                print(f"Email of customer is: {email}")
                email = input("What would you like the new email of customer be?:  ")
                new_data.append({"name": name, "age": age, "id": id, "phone": phone, "email": email})
                print("\n")

                i = i + 1
            else:
                new_data.append(customer)
                i = i + 1
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print("Customer updated successfully")

    else:
        print("Invalid input try again")
        update_customer()


def return_customer_name():
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_all_customers()
        new_data = []
        f = open(file_path, 'r')
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
                phone = customer["phone"]
                email = customer["email"]
                print(f"Name of customer is:  {name}")
                name = input("What would you like the new name of customer be?:  ")
                print(f"Age of customer is: {age}")
                age = int(input("What would you like the new age of customer be?:  "))
                print(f"ID of customer is: {id}")
                age = input("What would you like the new ID of customer be?:  ")
                print(f"Phone No of customer is: {phone}")
                phone = input("What would you like the new Phone No of customer be?:  ")
                print(f"Email of customer is: {email}")
                email = input("What would you like the new email of customer be?:  ")
                new_data.append({"name": name, "age": age, "id": id, "phone": phone, "email": email})
                print("\n")

                i = i + 1
            else:
                new_data.append(customer)
                i = i + 1
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print("Customer updated successfully")

    else:
        print("Invalid input try again")
        update_customer()


# add_customer()
# update_customer()