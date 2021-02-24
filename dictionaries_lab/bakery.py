products_in_bakery = input().split()
bakery = {}

for i in range(0, len(products_in_bakery), 2):
    key = products_in_bakery[i]
    value = products_in_bakery[i + 1]
    bakery[key] = int(value)
print(bakery)