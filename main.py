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


# import random
# import openpyxl

# def generate_random_numbers(num_numbers, start_range, end_range):
#     random_numbers = [random.randint(start_range, end_range) for _ in range(num_numbers)]
#     return random_numbers

# def export_to_excel(numbers):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active

#     for row_num, number in enumerate(numbers, start=1):
#         cell = sheet.cell(row=row_num, column=1, value=number)

#     workbook.save("random_numbers.xlsx")
#     print("Random numbers exported to random_numbers.xlsx")

# if __name__ == "__main__":
#     num_numbers = 800
#     start_range = 15000000
#     end_range = 37000000

#     random_numbers = generate_random_numbers(num_numbers, start_range, end_range)
#     export_to_excel(random_numbers)


# import re

# def is_valid_plate(plate):
#     # Define a regex pattern to match valid number plates
#     pattern = re.compile(r'^K(?![A-Z]{2}\s000[A-Z])\w{3}\s[1-9]\d{2}[1-9][A-Z]$')
#     return bool(pattern.match(plate))

# def generate_number_plates():
#     # Initialize a count variable to keep track of the valid plates
#     count = 0

#     # Loop through all possible combinations and check if they match the pattern
#     for letter1 in range(ord('K'), ord('L')):
#         for letter2 in range(ord('A'), ord('Z') + 1):
#             for letter3 in range(ord('A'), ord('Z') + 1):
#                 for number1 in range(1, 10):
#                     for number2 in range(10):
#                         for letter4 in range(ord('A'), ord('Z') + 1):
#                             plate = f"{chr(letter1)}{chr(letter2)}{chr(letter3)} {number1:03d}{number2}{chr(letter4)}"
#                             if is_valid_plate(plate):
#                                 count += 1
#                                 print(plate)

#     return count

# total_valid_plates = generate_number_plates()
# print(f"Total valid plates: {total_valid_plates}")


# def generate_valid_plates():
#     valid_plates = []

#     for letter1 in range(ord('K'), ord('L')):
#         for letter2 in range(ord('A'), ord('Z') + 1):
#             for letter3 in range(ord('A'), ord('Z') + 1):
#                 for number1 in range(10):
#                     for number2 in range(10):
#                         for number3 in range(10):
#                             for letter4 in range(ord('A'), ord('Z') + 1):
#                                 plate = f"{chr(letter1)}{chr(letter2)}{chr(letter3)} {number1}{number2}{number3}{chr(letter4)}"
#                                 if "000" not in plate:
#                                     valid_plates.append(plate)

#     return valid_plates

# valid_plates = generate_valid_plates()
# total_valid_plates = len(valid_plates)

# for plate in valid_plates:
#     print(plate)

# print(f"Total valid plates: {total_valid_plates}")


import time

# def generate_valid_plates():
#     valid_plates = []

#     for letter1 in range(ord('K'), ord('L')):
#         for letter2 in range(ord('A'), ord('Z') + 1):
#             for letter3 in range(ord('A'), ord('Z') + 1):
#                 for number1 in range(10):
#                     for number2 in range(10):
#                         for number3 in range(10):
#                             for letter4 in range(ord('A'), ord('Z') + 1):
#                                 plate = f"{chr(letter1)}{chr(letter2)}{chr(letter3)} {number1}{number2}{number3}{chr(letter4)}"
#                                 if "000" not in plate and not plate.startswith("KDF"):
#                                     valid_plates.append(plate)

#     return valid_plates

# start_time = time.time()
# valid_plates = generate_valid_plates()
# end_time = time.time()

# total_valid_plates = len(valid_plates)

# for plate in valid_plates:
#     print(plate)

# execution_time_minutes = (end_time - start_time) / 60
# print(f"Total valid plates: {total_valid_plates}")
# print(f"Total execution time (minutes): {execution_time_minutes:.2f} minutes")

# import time
# import itertools

# def generate_valid_plates():
#     valid_plates = []
    
#     letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
#     numbers = [str(i) for i in range(10)]

#     for plate in itertools.product(letters, repeat=4):
#         for num in range(1, 1000):
#             plate_str = f"K{''.join(plate)} {num:03d}A"
#             if "000" not in plate_str and not plate_str.startswith("KDF"):
#                 valid_plates.append(plate_str)

#     return valid_plates

# start_time = time.time()
# valid_plates = generate_valid_plates()
# end_time = time.time()

# for plate in valid_plates:
#     print(plate)

# total_valid_plates = len(valid_plates)
# print(f"Total valid plates: {total_valid_plates}")
# print(f"Total execution time (seconds): {end_time - start_time:.2f} seconds")

