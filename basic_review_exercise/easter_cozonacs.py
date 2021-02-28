budget = float(input())
flour_price = float(input())
pack_of_eggs_price = flour_price * 0.75
milk_for_one_cozonac = flour_price * 1.25 / 4
cozonac_price = flour_price + pack_of_eggs_price + milk_for_one_cozonac
colored_eggs = 0
number_of_cozonacs = 0
current_price = 0
while budget - cozonac_price > 0:
    budget -= cozonac_price
    colored_eggs += 3
    number_of_cozonacs += 1
    if number_of_cozonacs % 3 == 0:
        colored_eggs -= number_of_cozonacs - 2
difference = budget - current_price
print(f"You made {number_of_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {difference:.2f}BGN left.")
