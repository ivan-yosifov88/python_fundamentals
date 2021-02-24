numbers = [1, 2, 2, 3, 4, "abs", "abs", 5, 5, 6]

rev_nums = []
for num in range(len(numbers)- 1, -1, -1):
    rev_nums.append(numbers[num])
ord_set = list(set(rev_nums))
print(ord_set)