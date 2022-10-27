import json

product_file = "/home/moringa/PycharmProjects/SEPA/sprint_one/product/products.json"


def search_product_by_id(id):
    product = []
    file = open(product_file, 'r')
    if product_file == 0:
        product = []
    else:
        products = json.load(file)
        for each in products:
            if each.get("id") == id:
                product = each
                print(product)
            else:
                print("product does not exist")
                break
    return product


# fetch_product_by_id(23)
