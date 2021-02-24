import re
total_price = 0
products_list = []
line = input()
pattern = r"^>>(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)($|\s)"
while not line == "Purchase":
    products = re.match(pattern, line)
    if products:
        name = products.groupdict()
        products_list.append(products['name'])
        total_price += float(products['price']) * int(products['quantity'])
    line = input()

print("Bought furniture:")
for name in products_list:
    print(name)
print(f"Total money spend: {total_price:.2f}")


