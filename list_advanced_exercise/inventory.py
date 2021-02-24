collect_items = input().split(", ")

command = input()
while not command == "Craft!":
    new_command, item = command.split(" - ")

    if new_command == "Collect":
        if item not in collect_items:
            collect_items.append(item)
    elif new_command == "Drop":
        if item in collect_items:
            collect_items.remove(item)
    elif new_command == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collect_items:
            index_old_item = collect_items.index(old_item)
            collect_items.insert(index_old_item + 1 , new_item)
    elif new_command == "Renew":
        if item in collect_items:
            index_to_renew = collect_items.index(item)
            collect_items.pop(index_to_renew)
            collect_items.append(item)

    command = input()

print(", ".join(collect_items))

