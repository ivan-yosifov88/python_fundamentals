number_of_rows = int(input())

positive_numbers_list = []
negative_numbers_list = []
count_positive_numbers = 0
sum_of_negative_numbers = 0

for rows in range(number_of_rows):
    new_number = int(input())
    if new_number < 0:
        sum_of_negative_numbers += new_number
        negative_numbers_list.append(new_number)
    else:
        count_positive_numbers += 1
        positive_numbers_list.append(new_number)
print(positive_numbers_list)
print(negative_numbers_list)
# print(f"Count of positives: {count_positive_numbers}. Sum of negatives: {sum_of_negative_numbers}")
print(f"Count of positives: {len(positive_numbers_list)}. Sum of negatives: {sum(negative_numbers_list)}")