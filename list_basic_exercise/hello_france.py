items_price_list = input().split("|")
budget = float(input())
start_budget = budget
list_for_sale = []


for couples in items_price_list:
    items, price = couples.split("->")
    price = float(price)
    if items == "Clothes" and price > 50:
        continue
    elif items == "Shoes" and price > 35:
        continue
    elif items == "Accessories" and price > 20.5:
        continue

    if budget >= price:
        budget -= price
        price *= 1.4
        list_for_sale.append(price)

for numbers in list_for_sale:
    print(f"{numbers:.2f}", end=" ")
print()

print(f"Profit: {(sum(list_for_sale) - start_budget + budget):.2f}")
if sum(list_for_sale) + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")