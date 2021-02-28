train_length = int(input())
wagons = [0] * train_length

while True:
    command = input()
    token = command.split()[0]
    if command == "End":
        break
    elif token == "add":
        people = int(command.split()[1])
        wagons[-1] += people
    elif token == "insert":
        index = int(command.split()[1])
        people = int(command.split()[2])
        wagons[index] += people
    elif token == "leave":
        index = int(command.split()[1])
        people = int(command.split()[2])
        wagons[index] -= people
print(wagons)