#`COMMAND-LINE POINT-OF-SALE PROGRAM IN PYTHON`
## SEPA Program Sprint one
# Sprint Deliverables
- Develop a POS system using python
- Validate input data

## About the POS
POS Console App is a Command - Line based Point Of Sale System. The project was developed using Python programming language. It is a single user application meant to operate in a sales store or shops. The system facilitates for CRUD operations for both customers and products, and further supports purchase functionalities. The project objectives were to achieve a menu-driven system based on user's input that further executes its sub-programs associated with the menu. The details in the process were captured in a JSON file.


## Table of contents
* [About the POS](#About the POS)
* [Technologies](#Technologies)
* [Features](#Features)
* [Setup](#Setup)

## Technologies
* Language: [Python 3.8](https://www.python.org/downloads/release/python-3810/)
* IDE: [Pycharm](https://www.jetbrains.com/help/pycharm/quick-start-guide.html)

## Features
## Main Menu
A menu when the app is launched. It contains Customer Menu, Product Menu and Shopping Menu.
### Customer Operations
A user is able to feed into the system customer data, view available customers, update existing customer data and delete a particular customer. All customer records can further be accessed.
### Product Operations
A user can key in the product's data for inventory purposes, view the available products, update product data and delete a product.
### Purchase function
Customer details were first retrieved then added to the ongoing purchase, the user then adds the products and the quantities that the customer has ordered into a cart. In the process the subtotal of all products are calculated. During checkout, the total cost is calculated, product quantity decremented for the remaining products in the store and a receipt issued to the customer. The data captured in the cart is used to generate a purchase log that can later be viewed. The cart is then emptied to make room for future purchases. The purchase log generated contains the orders that were made from different purchases, the customers in-charge, purchased products and total amounts.

## Setup
### Requirements
Python 3 is required to be installed in your system. Depending on your operating system, you can download one that is compatible from the [Official Python website](https://www.python.org/downloads/) 
### Installation
To install this application, one is required to clone this repo by running the following command on your terminal:
```bash 
git clone https://github.com/VincentLangat033/sprint-one-python-POS-CLI
```
Then enter the folder of the application by running:
```bash 
cd point-of-sale-terminal
```
Start the program by running the following command:
```bash 
python main.py
```
