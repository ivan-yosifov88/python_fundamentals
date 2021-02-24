legendary_dictionary = {"shards": 0, "fragments": 0, "motes": 0}
junk_dictionary = {}
winner = ""
while winner == "":
    legendary_list = input().lower().split()
    for index in range(0, len(legendary_list), 2):
        quantity = int(legendary_list[index])
        material = legendary_list[index + 1]
        if material not in legendary_dictionary:
            if material not in junk_dictionary:
                junk_dictionary[material] = quantity
            else:
                junk_dictionary[material] += quantity
        else:
            legendary_dictionary[material] += quantity
            if legendary_dictionary[material] >= 250:
                legendary_dictionary[material] -= 250
                winner = material
                break
if winner == "shards":
    print("Shadowmourne obtained!")
elif winner == "fragments":
    print("Valanyr obtained!")
elif winner == "motes":
    print("Dragonwrath obtained!")

sorted_legendary_dictionary = dict(sorted(legendary_dictionary.items(), key=lambda x: (-x[1], x[0])))
sorted_junk_dictionary = dict(sorted(junk_dictionary.items(), key=lambda x: x[0]))
for material, quantity in sorted_legendary_dictionary.items():
    print(f"{material}: {quantity}")
for junk_material, junk_quantity in sorted_junk_dictionary.items():
    print(f"{junk_material}: {junk_quantity}")