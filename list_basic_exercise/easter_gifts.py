names_of_the_gifts = input().split()
command = input()

while not command == "No Money":
    commands = command.split()
    if commands[0] == "OutOfStock":
        for index in range(len(names_of_the_gifts)):
            if commands[1] == names_of_the_gifts[index]:
                names_of_the_gifts[index] = None
    elif commands[0] == "Required":
        for index in range(len(names_of_the_gifts)):
            if int(commands[2]) == index:
                names_of_the_gifts[index] = commands[1]
    elif commands[0] == "JustInCase":
        names_of_the_gifts.pop()
        names_of_the_gifts.append(commands[1])
        # for index in range(len(names_of_the_gifts)):
        #     commands[1]
    command = input()
for values in names_of_the_gifts:
    if None in names_of_the_gifts:
        names_of_the_gifts.remove(None)
print(*names_of_the_gifts)