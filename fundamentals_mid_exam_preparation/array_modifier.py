array_values = [int(element) for element in input().split(" ")]

command = input()
while not command == "end":
    command.split(" ")
    data = command.split(" ")[0]
    if data == "swap" or data == "multiply":
        index_a = command.split(" ")[1]
        index_a = int(index_a)
        index_b = command.split(" ")[2]
        index_b = int(index_b)
    if data == "swap":
        array_values[index_a], array_values[index_b] = array_values[index_b], array_values[index_a]
    elif data == "multiply":
        array_values[index_a] = array_values[index_a] * array_values[index_b]
    elif data == "decrease":
        for i in range(len(array_values)):
            array_values[i] -= 1

    command = input()

array_values = [str(values) for values in array_values]
print(", ".join(array_values))
