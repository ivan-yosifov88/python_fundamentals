def loading_bar(num):
    number_percent = num // 10
    number_dots = 10 - number_percent
    number_percent_symbol = number_percent * "%"
    number_dots_symbol = number_dots * "."
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{num}% [{number_percent_symbol}{number_dots_symbol}]")
        print("Still loading...")

number = int(input())
loading_bar(number)