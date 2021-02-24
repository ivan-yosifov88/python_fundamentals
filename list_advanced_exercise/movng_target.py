
def shoot_command(num_list, i, v):
    if 0 <= i < len(num_list):
        num_list[i] -= v
        if num_list[i] <= 0:
            num_list.remove(num_list[i])
    return num_list


def add_command(num_list, i, v):
    if 0 <= i < len(num_list):
        num_list.insert(i, v)
    else:
        print("Invalid placement!")
    return num_list


def strike_command(num_list, i, v):
    first_part = i - v
    second_part = i + v
    if first_part >= 0 and second_part < len(num_list):
        num_list = num_list[:first_part] + num_list[second_part + 1:]

    else:
        print("Strike missed!")
    return num_list


sequence_of_targets = input().split()

sequence_of_targets = [int(num) for num in sequence_of_targets]
command = input()
while not command == "End":
    data, index, value = command.split()
    index = int(index)
    value = int(value)
    if data == "Shoot":
        sequence_of_targets = shoot_command(sequence_of_targets, index, value)
    elif data == "Add":
        sequence_of_targets = add_command(sequence_of_targets, index, value)
    elif data == "Strike":
        sequence_of_targets = strike_command(sequence_of_targets, index, value)
    command = input()

print("|".join(str(el) for el in sequence_of_targets))