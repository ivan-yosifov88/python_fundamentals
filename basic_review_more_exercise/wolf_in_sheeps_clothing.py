list_of_animals = input().split(", ")
list_of_sheep = []
if list_of_animals[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    list_of_animals.reverse()
    for index in range(1, len(list_of_animals) + 1):
        if list_of_animals[index] == "wolf":
            print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")
            break

