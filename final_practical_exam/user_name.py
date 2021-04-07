def case_command(user, command_info):
    if command_info == "lower":
        user = user.lower()
    elif command_info == "upper":
        user = user.upper()
    return user


def is_indices_valid(user, start, end):
    if start in range(len(user)) and end in range(len(user)):
        return True
    return False


def reverse_command(user, start, end):
    if is_indices_valid(user, start, end):
        substring = user[start:end + 1]
        print(substring[::-1])


def cut_command(user, command_info):
    if command_info in user:
        user = user.replace(command_info, "")
        print(user)
    else:
        print(f"The word {user} doesn't contain {command_info}.")
    return user


def replace_command(user, char):
    user = user.replace(char, "*")
    return user


def check_command(user, char):
    if char in user:
        print("Valid")
    else:
        print(f"Your username must contain {char}.")


username = input().strip()

data = input()

while not data == "Sign up":
    info = data.split()
    command = info[0]
    if command == "Case":
        username = case_command(username, info[1])
        print(username)
    elif command == "Reverse":
        start_index = int(info[1])
        end_index = int(info[2])
        reverse_command(username, start_index, end_index)
    elif command == "Cut":
        username = cut_command(username, info[1])
    elif command == "Replace":
        username = replace_command(username, info[1])
        print(username)
    elif command == "Check":
        check_command(username, info[1])

    data = input()
