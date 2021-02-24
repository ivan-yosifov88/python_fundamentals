def sum_numbers(a, b):
    sum_result = a + b
    return sum_result


def subtract(sum_result, c):
    sub_result = sum_result - c
    return sub_result


def add_and_subtract(a, b, c):
    result = None
    result = subtract(sum_numbers(a, b), c)
    return result



first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
