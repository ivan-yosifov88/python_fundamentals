list_of_numbers = input().split()
step_value = int(input())
permutation_list = []
counter = 0
index = 0
while len(list_of_numbers) > 0:
    counter += 1
    if counter % step_value == 0:
        number = list_of_numbers.pop(index)
        permutation_list.append(number)
    else:
        index += 1
    if index >= len(list_of_numbers):
        index = 0

print(f"[{','.join(permutation_list)}]")