command = input()

list_of_resources = []
while not command == "stop":
    list_of_resources.append(command)
    command = input()

resources_dictionary = {}
for index in range(0, len(list_of_resources), 2):
    resource = list_of_resources[index]
    quantity = int(list_of_resources[index + 1])
    if resource not in resources_dictionary:
        resources_dictionary[resource] = quantity
    else:
        resources_dictionary[resource] += quantity

for resource, quantity in resources_dictionary.items():
    print(f"{resource} -> {quantity}")