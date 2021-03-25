def is_plant_valid(plant_dict, plant_name):
    if plant_name in plant_dict:
        return True
    else:
        print("error")
    return False


def rate_command(plant_dict, new_command):
    plant_name, add_rating = new_command.split(" - ")
    add_rating = int(add_rating)
    if is_plant_valid(plant_dict, plant_name):
        plant_dict[plant_name]['rating'].append(add_rating)
    return plant_dict


def update_command(plants_dict, new_command):
    plant_name, new_rarity = new_command.split(" - ")
    if is_plant_valid(plants_dict, plant_name):
        plants_dict[plant_name]['rarity'] = int(new_rarity)
    return plants_dict


def reset_command(plants_dict, new_command):
    plant_name = new_command
    if is_plant_valid(plants_dict, plant_name):
        if "rating" in plants_dict[plant_name]:
            plants_dict[plant_name]["rating"] = []
    return plants_dict


number_of_plants = int(input())

plants_collection = {}

for _ in range(number_of_plants):
    plant, rarity = input().split("<->")
    plants_collection[plant] = {"rarity": int(rarity), "rating": []}

data = input()

while not data == "Exhibition":
    command, info = data.split(": ")

    if command == "Rate":
        rate_command(plants_collection, info)
    elif command == "Update":
        update_command(plants_collection, info)
    elif command == "Reset":
        reset_command(plants_collection, info)
    data = input()

for p in plants_collection:
    if plants_collection[p]["rating"]:
        plants_collection[p]["rating"] = sum(plants_collection[p]["rating"]) / len(plants_collection[p]["rating"])
    else:
        plants_collection[p]["rating"] = 0
sorted_plants_collection = sorted(plants_collection.items(), key=lambda x: (-x[1]['rarity'], -x[1]['rating']))

print("Plants for the exhibition:")
for pl in sorted_plants_collection:
    print(f"- {pl[0]}; Rarity: {pl[1]['rarity']}; Rating: {pl[1]['rating']:.2f}")