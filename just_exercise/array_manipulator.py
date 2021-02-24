def add_command(num_list, i, el):
    num_list.insert(i, el)
    return num_list


def add_many_command(num_list, i, el):
    num_list = num_list[:i] + el + num_list[i:]
    return num_list


def contain_command(num_list, el):
    if el in num_list:
        return num_list.index(el)
    else:
        return -1


def remove_command(num_list, el):
    result = num_list.pop(el)
    return num_list


def shift_command(num_list, pos):
    while pos > 0:
        removed = num_list.pop(0)
        num_list.append(removed)
        pos -= 1
    return num_list


def sum_pairs_command(num_list):
    result_list = []
    if len(num_list) % 2 == 0:
        for i in range(0, len(num_list), 2):
            result = num_list[i] + num_list[i + 1]
            result_list.append(result)
    else:
        for i in range(0, len(num_list) - 1, 2):
            result = num_list[i] + num_list[i + 1]
            result_list.append(result)
        result_list.append(num_list[-1])
    return result_list


line_of_integers = list(map(int, input().split()))

data = input()
while not data == "print":
    new_command = data.split()
    command = new_command[0]
    if command == "add":
        index, element = new_command[1:]
        index = int(index)
        element = int(element)
        line_of_integers = add_command(line_of_integers, index, element)
    elif command == "addMany":
        index = new_command[1]
        index = int(index)
        list_nums = new_command[2:]
        list_nums = list(map(int, list_nums))
        line_of_integers = add_many_command(line_of_integers, index, list_nums)
    elif command == "contains":
        element = int(new_command[1])
        print(contain_command(line_of_integers,element))
    elif command == "remove":
        element = int(new_command[1])
        line_of_integers = remove_command(line_of_integers, element)
    elif command == "shift":
        position = int(new_command[1])
        line_of_integers = shift_command(line_of_integers, position)
    elif command == "sumPairs":
        line_of_integers = sum_pairs_command(line_of_integers)
    data = input()

print(line_of_integers)