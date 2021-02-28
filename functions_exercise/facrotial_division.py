def factorial_divisor(a, b):
    factorial_num_a = 1
    for num_a in range(2, a + 1):
        factorial_num_a *= num_a

    factorial_num_b = 1
    for num_b in range(2, b + 1):
        factorial_num_b *= num_b

    result = factorial_num_a / factorial_num_b

    print(f"{result:.2f}")


first_number = int(input())
second_number = int(input())

factorial_divisor(first_number, second_number)