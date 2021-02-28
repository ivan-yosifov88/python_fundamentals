string_line = input()
explosion = 0
index = 0
while index < len(string_line):
    element = string_line[index]

    if element == ">":
        explosion += int(string_line[index + 1])
    elif explosion > 0:
        string_line = string_line[:index] + string_line[index + 1:]
        index -= 1
        explosion -= 1
    index += 1

print(string_line)