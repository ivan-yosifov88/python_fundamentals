def is_index_valid(string_line, current_index):
    if 0 <= current_index < len(string_line):
        return True


def add_stop_command(string_line, get_info):
    index, string_to_insert = get_info
    index = int(index)
    if is_index_valid(string_line, index):
        string_line = string_line[:index] + string_to_insert + string_line[index:]
    return string_line


def remove_stop_command(string_line, get_info):
    start_index, end_index = get_info
    start_index = int(start_index)
    end_index = int(end_index)
    if is_index_valid(string_line, start_index) and is_index_valid(string_line, end_index):
        string_line = string_line[:start_index] + string_line[end_index+1:]
    return string_line


def switch_command(string_line, get_info):
    old_string, new_string = get_info
    if old_string in string_line:
        string_line = string_line.replace(old_string, new_string)
    return string_line


destinations = input()

data = input()

while not data == "Travel":
    command = data.split(":")[0]
    if command == "Add Stop":
        info = data.split(":")[1:]
        destinations = add_stop_command(destinations, info)
    elif command == "Remove Stop":
        info = data.split(":")[1:]
        destinations = remove_stop_command(destinations, info)
    elif command == "Switch":
        info = data.split(":")[1:]
        destinations = switch_command(destinations, info)
    print(destinations)
    data = input()

print(f"Ready for world tour! Planned stops: {destinations}")