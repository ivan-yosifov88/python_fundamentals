def take_odd_command(line):
    line = ''.join(line[i] for i in range(len(line)) if i % 2 == 1 )
    return line


def cut_command(line, data):
    index, length = data
    index = int(index)
    length = int(length)
    substring = line[index:index + length]
    if substring in line:
        line = line.replace(substring, "", 1)
    return line


def substitute_command(line, data):
    substring, substitute = data
    if substring in line:
        while substring in line:
            line = line.replace(substring, substitute)
        print(line)
    else:
        print("Nothing to replace!")
    return line
string_line = input()

command = input()

while not command == "Done":
    if command == "TakeOdd":
        string_line = take_odd_command(string_line)
        print(string_line)

    elif command.split()[0] == "Cut":
        data = command.split()[1:]
        string_line = cut_command(string_line, data)
        print(string_line)
    elif command.split()[0] == "Substitute":
        data = command.split()[1:]
        string_line = substitute_command(string_line, data)
    command = input()

print(f"Your password is: {string_line}")