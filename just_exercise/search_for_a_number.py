list_of_numbers = list(map(int, input().split()))
index, element_to_delete, number_to_check = input().split()
index = int(index)
element_to_delete = int(element_to_delete)
number_to_check = int(number_to_check)

changed_list = list_of_numbers[element_to_delete:index]

manipulated_list = changed_list + list_of_numbers[index:]

if number_to_check in manipulated_list:
    print("YES!")
else:
    print("NO!")