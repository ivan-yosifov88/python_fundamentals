# number_string = input()
# number_string_as_list = number_string.split()
# invert_list = []
# for index in range(len(number_string_as_list)):
#     new_number = (number_string_as_list[index])
#     invert_list.append(int(new_number) * -1)
# print(invert_list)

numbers = input().split()

new_list = []
for nums in numbers:
    number = int(nums)
    number *= -1
    new_list.append(number)
print(new_list)