def move_command(message, command_info):
    number_of_letters = int(command_info)
    message = message[number_of_letters:] + message[:number_of_letters]
    return message


def insert_command(message, command_info):
    index, value = command_info
    index = int(index)
    message = message[:index] + value + message[index:]
    return message


def change_all_command(message, command_info):
    substring, replacement = command_info
    if substring in message:
        message = message.replace(substring, replacement)
    return message


encrypted_message = input()

data = input()

while not data == "Decode":
    info = data.split("|")
    command = info[0]
    if command == "Move":
        new_data = info[1]
        encrypted_message = move_command(encrypted_message, new_data)
    elif command == "Insert":
        new_data = info[1:]
        encrypted_message = insert_command(encrypted_message, new_data)
    elif command == "ChangeAll":
        new_data = info[1:]
        encrypted_message = change_all_command(encrypted_message, new_data)
    data = input()

print(f"The decrypted message is: {encrypted_message}")