treasure_chest = input().split("|")

data = input()

while not data == "Yohoho!":
    command = data.split()[0]
    if command == "Loot":
        items = data.split()[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)
    elif command == "Drop":
        index = data.split()[1]
        index = int(index)
        if 0 <= index < len(treasure_chest):
            element = treasure_chest.pop(index)
            treasure_chest.append(element)
    elif command == "Steal":
        count = data.split()[1]
        count = int(count)
        steal_count = []
        if count >= len(treasure_chest):
            count = len(treasure_chest)
        for element in range(count):
            steal_count.insert(0, treasure_chest[-1])
            treasure_chest.pop(-1)
        print(*steal_count, sep=", ")

    data = input()

if treasure_chest:
    average_gain = 0
    for loot in treasure_chest:
        average_gain += len(loot)
    average_gain /= len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")