# from termcolor import colored

# pos_cli = ("""
# ----------------------------------

# *** Dear Customer, ***
# ----------------------------------

# *** Welcome to Python POS CLI  ***

# ----------------------------------
# *** You will perform the following operations ***
#     """)


# def main_menu():

#     print(colored(pos_cli, "yellow"))
#     print(colored("1. Customer Operations ", "blue"))
#     print(colored("2. Product Operations ", "blue"))
#     print(colored("3. Purchase Operations", "blue"))
#     print(colored("""
# ________________________________________________
#     """, "yellow"))
#     print(colored("What do you wish to do? ", "blue"))
#     value = int(input(colored("Enter operation you wish to perform : ", "blue")))
#     if value == 1:
#         print(colored("""
# ---------------------------------------------

# ***   You are at  Customer Operations Column:   ***
    
# ---------------------------------------------
#         """, "yellow"))
#         from customer import customer_menu
#         customer_menu.customer_menu()
#     elif value == 2:
#         from product import product_menu
#         product_menu.product_menu()
#     elif value == 3:
#         from purchases import purchase_menu
#         purchase_menu.make_purchases()
 
#     else:
#         print("""
# `````````````````````````````
#         """)
#         print(colored("Try again", "red"))
#         main_menu()


# main_menu()


import random
import openpyxl

def generate_random_numbers(num_numbers, start_range, end_range):
    random_numbers = [random.randint(start_range, end_range) for _ in range(num_numbers)]
    return random_numbers

def export_to_excel(numbers):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for row_num, number in enumerate(numbers, start=1):
        cell = sheet.cell(row=row_num, column=1, value=number)

    workbook.save("random_numbers.xlsx")
    print("Random numbers exported to random_numbers.xlsx")

if __name__ == "__main__":
    num_numbers = 800
    start_range = 15000000
    end_range = 37000000

    random_numbers = generate_random_numbers(num_numbers, start_range, end_range)
    export_to_excel(random_numbers)

