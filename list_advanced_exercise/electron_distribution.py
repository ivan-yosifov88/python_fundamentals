electrons_number = int(input())

electron_shell_list = []
index = 1
while electrons_number > 0:
    current_shell = 2 * index ** 2
    if electrons_number > current_shell:
        electron_shell_list.append(current_shell)
    else:
        electron_shell_list.append(electrons_number)
    index += 1
    electrons_number -= current_shell

print(electron_shell_list)
