import json
import re
from termcolor import colored
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
    customer = {"name": input(colored("Enter Name: ", "blue")), "age": int(input(colored("Age: ", "blue"))),
                "id": input(colored("Customer ID: ", "blue"))}
    while True:
        email = input(colored("Customer Email: ", "yellow"))
        if solve(email):
            customer["email"] = email
            break
        else:
            print(colored("Enter the correct email format!", "red"))
            continue
    while True:
        phone = input(colored("Enter Phone Number: ", "yellow"))
        if validate_phone(phone):
            customer["phone"] = phone
            break
        else:
            print(colored("Phone number should start with 0 !", "red"))
            continue
    customers.append(customer)

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(customers, json_file, indent=4, separators=(',', ': '))
        print(colored("Customer created successfully", "yellow"))
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
        print(colored(f"Index of this customer is :  {i}", "yellow"))
        print(colored(f"Name of customer :  {name}", "blue"))
        print(colored(f"Age of customer:  {age}", "blue"))
        print(colored(f"Email of customer: {email}", "yellow"))
        print(colored(f"Phone number of customer:  {phone}", "blue"))
        print(colored(f"The ID of customer: {id}", "blue"))
        print(colored("""
____________________________________________________
        """, "blue"))
        i = i+1


def delete_customer():
    print(colored("""
       Want to delete a customer?
   Press 1 to view index of Customer you want to delete:
    
    """, "blue"))

    user_input = input(colored("Enter value to proceed: ", "blue"))
    if user_input == "1":
        view_all_customers()
        new_data = []
        f = open(file_path, 'r')
        customers = json.load(f)
        data_length = len(customers)-1
        print(colored("Which index would you like to delete?", "yellow"))
        delete_option = input(colored(f"Select a number between 0 and {data_length}: ", "blue"))
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
            print(colored("Customer deleted successfully", "yellow"))

    else:
        print(colored("Invalid input try again", "red"))
        delete_customer()


def update_customer():

    print(colored("""
```````````````````````````````````````
***  Customer Update Section   ***

 Want to update a customer?
 Press 1 to view index of Customer you want to update:
 Press 2 to return to Customer Menu
 Press 3 to exit the program at this stage
 
 ````````````````````````````````````````
""", "blue"))
    user_input = input(colored("Enter value to proceed: ", "blue"))
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
                print(colored(f"Name of customer is:  {name}", "yellow"))
                name = input(colored("What would you like the new name of customer be?:  ", "blue"))
                print(colored(f"Age of customer is: {age}", "yellow"))
                age = int(input(colored("What would you like the new age of customer be?:  ", "blue")))
                print(colored(f"ID of customer is: {id}", "yellow"))
                id = input(colored("What would you like the new ID of customer be?:  ", "blue"))
                print(colored(f"Phone No of customer is: {phone}", "yellow"))
                phone = input(colored("What would you like the new Phone No of customer be?:  ", "blue"))
                print(colored(f"Email of customer is: {email}", "yellow"))
                email = input(colored("What would you like the new email of customer be?:  ", "blue"))
                new_data.append({"name": name, "age": age, "id": id, "phone": phone, "email": email})
                print("\n")

                i = i + 1
            else:
                new_data.append(customer)
                i = i + 1
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, indent=4, separators=(',', ': '))
            print(colored("Customer updated successfully", "yellow"))

    else:
        print(colored("Invalid input try again", "red"))
        update_customer()


def return_customer_name():
    user_input = input("Enter value to proceed: ")
    if user_input == "1":
        view_all_customers()
        new_data = []
        f = open(file_path, 'r')
        customers = json.load(f)
        data_length = len(customers) - 1
        print(colored("Which index would you like to update?", "blue"))
        edit_option = input(colored(f"Select a number between 0 and {data_length}: ", "blue"))
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
            print(colored("Customer updated successfully", "yellow"))

    else:
        print(colored("Invalid input try again", "red"))
        update_customer()


# add_customer()
# update_customer()