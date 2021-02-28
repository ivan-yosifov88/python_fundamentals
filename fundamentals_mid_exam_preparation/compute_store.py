command = input()

total_price = 0
while not (command == "regular" or command == "special"):
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        total_price += price
    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    amount_of_taxes = total_price * 0.2
    total_price_with_taxes = total_price + amount_of_taxes
    if command == "special":
        total_price_with_taxes *= 0.9
    print("Congratulations you've just bought a new computer!""\n"
          f"Price without taxes: {total_price:.2f}$""\n"
          f"Taxes: {amount_of_taxes:.2f}$""\n"
          "-----------""\n"
          f"Total price: {total_price_with_taxes:.2f}$")
