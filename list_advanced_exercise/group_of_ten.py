from math import ceil
list_of_numbers = list(map(int, input().split(", ")))

number_of_iterations = ceil(max(list_of_numbers) / 10)
previous_group = 0
for iterations in range(1, number_of_iterations + 1):
    group_type = iterations * 10
    current_list = []
    for nums in list_of_numbers:
        if group_type >= nums > previous_group:
            current_list.append(nums)
    print(f"Group of {iterations}0's: {current_list}")
    previous_group = group_type