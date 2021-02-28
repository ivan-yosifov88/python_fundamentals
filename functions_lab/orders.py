def order_price(product, quantity):
    price = None
    if product == "coffee":
        price = quantity * 1.50
    elif product == "water":
        price = quantity * 1.00
    elif product == "coke":
        price = quantity * 1.40
    elif product == "snacks":
        price = quantity * 2.00
    return price


type_of_product = input()
product_quantity = int(input())

print(f"{order_price(type_of_product, product_quantity):.2f}")

