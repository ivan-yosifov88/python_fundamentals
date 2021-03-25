def insert_space(message, instruction):
    index = int(instruction[0])
    message = message[:index] + " " + message[index:]
    return message


def reverse_command(message, instruction):
    substring = instruction[0]
    if substring in message:
        message = message.replace(substring, "", 1)
        message += substring[::-1]
        print(message)
    else:
        print("error")
    return message


def change_all(message, instruction):
    substring, new_substring = instruction
    message = message.replace(substring, new_substring)
    return message


concealed_message = input()

operation = input()

while not operation == "Reveal":
    command = operation.split(":|:")[0]
    data = operation.split(":|:")[1:]

    if command == "InsertSpace":
        concealed_message = insert_space_command = insert_space(concealed_message, data)
        print(insert_space_command)
    elif command == "Reverse":
        concealed_message = reverse_command(concealed_message, data)
    elif command == "ChangeAll":
        concealed_message = change_all(concealed_message, data)
        print(concealed_message)

    operation = input()

print(f"You have a new text message: {concealed_message}")