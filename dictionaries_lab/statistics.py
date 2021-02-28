command = input()

product_in_stock = {}
while not command == "statistics":
    product, quantity = command.split(": ")
    quantity = int(quantity)
    if product not in product_in_stock:
        product_in_stock[product] = quantity
    else:
        product_in_stock[product] += quantity
    command = input()

print("Products in stock:")
for product, quantity in product_in_stock.items():
    print(f"- {product}: {quantity}")
# print(f"Total Products: {len(product_in_stock.keys())}")
print(f"Total Products: {len(product_in_stock)}")
print(f"Total Quantity: {sum(product_in_stock.values())}")

