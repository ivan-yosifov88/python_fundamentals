import sys

list_of_integer = input().split()
number_to_remove = int(input())
new_list = []

for integer in list_of_integer:
    number = int(integer)
    new_list.append(number)

for iterations in range(number_to_remove):
    smallest_number = sys.maxsize

    for numbers in new_list:
        if numbers < smallest_number:
            smallest_number = numbers
    new_list.remove(smallest_number)
print(new_list)

