def simple_calculator(a, b, operator):
    result = 0
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a // b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b
    return result


operator = input()
first_number = int(input())
second_number = int(input())


print(simple_calculator(first_number, second_number, operator))