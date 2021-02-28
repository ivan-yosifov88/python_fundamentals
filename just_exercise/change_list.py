def delete(num_list, num):
    num_list = [number for number in num_list if not number == num ]
    return num_list

def insert(num_list, el, index):
    num_list.insert(index, el)
    return num_list

def even_or_odd_list(num_list, command):
    if command == "Even":
        return [number for number in num_list if number % 2 == 0]
    elif command == "Odd":
        return [number for number in num_list if number % 2 == 1]


number_list = [int(number) for number in input().split()]
command = input()

while not (command == "Odd" or command == "Even"):
    new_command , data = command.split(maxsplit=1)
    if new_command == "Delete":
        data = int(data)
        number_list = delete(number_list, data)
    elif new_command == "Insert":
        element, position = data.split()
        element = int(element)
        position = int(position)
        number_list = insert(number_list, element, position)
    command = input()

print(*even_or_odd_list(number_list, command))