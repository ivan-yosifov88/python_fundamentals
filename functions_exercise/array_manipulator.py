
def exchange(list_numbers, index):
    if 0 <= index < len(list_numbers):
        first_part = list_numbers[:index + 1]
        second_part = list_numbers[index + 1:]
        exchange_list = second_part + first_part
        return exchange_list
    else:
        print("Invalid index")
        return list_numbers


def even_numbers(list_numbers):
    even_num = [num for num in list_numbers if num % 2 == 0]
    return even_num


def odd_numbers(list_numbers):
    odd_num = [num for num in list_numbers if num % 2 == 1]
    return odd_num


def max_element(list_numbers, state):
    max_index = 0
    max_elements = 0
    max_number = 0
    if state == "even":
        max_elements = even_numbers(list_numbers)
    elif state == "odd":
        max_elements = odd_numbers(list_numbers)
    if len(max_elements) == 0:
        return "No matches"
    max_number = max(max_elements)

    for number in range(len(list_numbers) - 1, -1, -1):
        if list_numbers[number] == max_number:
            max_index = number
            break
    return max_index


def min_element(list_numbers, state):
    min_index = 0
    min_elements = 0
    min_number = 0
    if state == "even":
        min_elements = even_numbers(list_numbers)
    elif state == "odd":
        min_elements = odd_numbers(list_numbers)
    if len(min_elements) == 0:
        return "No matches"
    min_number = min(min_elements)

    for number in range(len(list_numbers) - 1, -1, -1):
        if list_numbers[number] == min_number:
            min_index = number
            break
    return min_index


def first_count(list_numbers, state, count):
    count_first_even = even_numbers(list_numbers)
    count_first_odd = odd_numbers(list_numbers)
    if count > len(list_numbers):
        return "Invalid count"
    if state == "even":
        result = count_first_even[:count]
    elif state == "odd":
        result = count_first_odd[:count]
    return result


def last_count(list_numbers, state, count):
    count_last_even = even_numbers(list_numbers)
    count_last_odd = odd_numbers(list_numbers)
    if count > len(list_numbers):
        return "Invalid count"
    if state == "even":
        result = count_last_even[-count:]
    elif state == "odd":
        result = count_last_odd[-count:]
    return result


numbers_as_sting = input().split()
numbers = [int(elements) for elements in numbers_as_sting]
command = input()

while not command == "end":
    if command.split()[0] == "exchange":
        index = int(command.split()[1])
        numbers = exchange(numbers, index)
    elif command.split()[0] == "max":
        if command.split()[1] == "even":
            max_even_index = max_element(numbers, command.split()[1])
            print(max_even_index)
        elif command.split()[1] == "odd":
            max_odd_index = max_element(numbers, command.split()[1])
            print(max_odd_index)
    elif command.split()[0] == "min":
        if command.split()[1] == "even":
            min_even_index = min_element(numbers, command.split()[1])
            print(min_even_index)
        elif command.split()[1] == "odd":
            min_odd_index = min_element(numbers, command.split()[1])
            print(min_odd_index)
    elif command.split()[0] == "first":
        if command.split()[2] == "even":
            first_even = first_count(numbers, command.split()[2], int(command.split()[1]))
            print(first_even)
        elif command.split()[2] == "odd":
            first_odd = first_count(numbers, command.split()[2], int(command.split()[1]))
            print(first_odd)
    elif command.split()[0] == "last":
        if command.split()[2] == "even":
            last_even = last_count(numbers, command.split()[2], int(command.split()[1]))
            print(last_even)
        elif command.split()[2] == "odd":
            last_odd = last_count(numbers, command.split()[2], int(command.split()[1]))
            print(last_odd)

    command = input()

print(numbers)