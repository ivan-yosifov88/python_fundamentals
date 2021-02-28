list_of_products = input().split()
stock = {}

for index in range(0, len(list_of_products), 2):
    product = list_of_products[index]
    quantity = int(list_of_products[index + 1])
    stock[product] = quantity

products_to_search = input().split()
for product in products_to_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


