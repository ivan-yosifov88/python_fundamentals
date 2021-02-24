list_of_numbers = [int(num) for num in input().split(", ")]
number_of_beggars = int(input())

beggars_sum = []

start_index = 0
for beggar in range(1, number_of_beggars + 1):
    current_sum = 0
    for i in range(start_index, len(list_of_numbers), number_of_beggars):
        current_sum += list_of_numbers[i]
    beggars_sum.append(current_sum)
    start_index += 1

print(beggars_sum)
