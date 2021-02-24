command = input()

product_dictionary = {}
while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in product_dictionary:
        product_dictionary[name] = []
        product_dictionary[name].append(price)
        product_dictionary[name].append(quantity)
    else:
        product_dictionary[name][1] += quantity
        if not product_dictionary[name][0] == price:
            product_dictionary[name][0] = price

    command = input()

for name, price_quantity in product_dictionary.items():
    total_price = price_quantity[0] * price_quantity[1]
    print(f"{name} -> {total_price:.2f}")