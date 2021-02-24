target_list = list(map(int, input().split(" ")))

command = input()
while not command == "End":
    index = int(command)
    if not (0 <= index < len(target_list)):
        command = input()
        continue
    if not target_list[index] == -1:
        current_target_value = target_list[index]
        target_list[index] = -1
        for i in range(len(target_list)):
            if target_list[i] == -1:
                continue
            if target_list[i] > current_target_value:
                target_list[i] -= current_target_value
            else:
                target_list[i] += current_target_value

    command = input()

count_of_shoot_targets = target_list.count(-1)
print(f"Shot targets: {count_of_shoot_targets} ->",end= " ")
print(*target_list)