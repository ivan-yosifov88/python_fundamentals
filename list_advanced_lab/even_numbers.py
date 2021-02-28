list_of_nums = input().split(", ")

num_list = [int(num) for num in list_of_nums]

even_list = [index for index in range(len(num_list)) if num_list[index] % 2 == 0]

print(even_list)