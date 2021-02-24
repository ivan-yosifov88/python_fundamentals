first_list = input().split()
second_list = input().split()
is_first_shorter = False

left_counter = 0
right_counter = 0
if len(first_list) >= len(second_list):
    iteration = len(second_list)
    slice_part = len(first_list) - len(second_list)
elif len(first_list) < len(second_list):
    is_first_shorter = True
    iteration = len(first_list)
    slice_part = len(second_list) - len(first_list)
    is_second_larger = True
for index in range(iteration):
    if is_first_shorter:
        if first_list[index] == second_list[index]:
            left_counter += 1
    else:
        if first_list[index] == second_list[index]:
            left_counter += 1
for i in range(iteration -1, -1, -1):
    if is_first_shorter:
        if first_list[i] == second_list[slice_part:][i]:
            right_counter += 1
    else:
        if first_list[slice_part:][i] == second_list[i]:
            right_counter += 1


if left_counter == 0 and right_counter == 0:
    print(left_counter)
elif left_counter >= right_counter:
    print(left_counter)
elif right_counter > left_counter:
    print(right_counter)

