list_of_numbers = input().split(", ")
list_of_integers = []

for numbers in list_of_numbers:
    number = int(numbers)
    list_of_integers.append(number)

number_of_zeros = list_of_integers.count(0)

for nums in list_of_integers:
    if 0 in list_of_integers:
        list_of_integers.remove(0)

for zeros in range(number_of_zeros):
    list_of_integers.append(0)

print(list_of_integers)