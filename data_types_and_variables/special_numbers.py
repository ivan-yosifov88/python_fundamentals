end_number = int(input())

for numbers in range(1, end_number + 1):
    # sum_of_digits = 0
    # digits = numbers
    # while digits > 0:
    #     sum_of_digits += digits % 10
    #     digits = int(digits / 10)
    numbers_as_string = str(numbers)
    sum_of_digits = 0
    for digit in numbers_as_string:
        sum_of_digits += int(digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{numbers} -> True")
    else:
        print(f"{numbers} -> False")