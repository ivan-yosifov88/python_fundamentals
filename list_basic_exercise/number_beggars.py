list_of_numbers = input().split(", ")
beggars_counter = int(input())
int_list = []

for numbers in list_of_numbers:
    number = int(numbers)
    int_list.append(number)

new_list = []

for elements in range(beggars_counter):
    new_list.append(0)

index = 0

for numbers in int_list:
    new_list[index] += numbers
    index += 1
    if index == beggars_counter:
        index = 0
print(new_list)

