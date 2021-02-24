factor_number = int(input())
counter_number = int(input())

result_number = 0
result_list = []

for index in range(1, counter_number + 1):
    result_number = factor_number * index
    result_list.append(result_number)
print(result_list)