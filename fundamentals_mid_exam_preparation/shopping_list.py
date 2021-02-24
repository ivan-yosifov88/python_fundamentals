shopping_list = [product for product in input().split("!")]

command = input()
while not command == "Go Shopping!":
    new_command = command.split(" ")
    data = new_command[0]
    if data == "Urgent":
        item = new_command[1]
        if item not in shopping_list:
            shopping_list.insert(0, item)
    elif data == "Unnecessary":
        item = new_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
    elif data == "Correct":
        old_item = new_command[1]
        new_item = new_command[2]
        if old_item in shopping_list:
            index_of_item = shopping_list.index(old_item)
            shopping_list.remove(old_item)
            shopping_list.insert(index_of_item, new_item)
    elif data == "Rearrange":
        item = new_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
            shopping_list.append(item)

    command = input()

print(", ".join(shopping_list))

