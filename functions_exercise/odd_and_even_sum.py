def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for digits in number:
        if int(digits) % 2 == 0:
            even_sum += int(digits)
        else:
            odd_sum += int(digits)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()

odd_even_sum(number)
