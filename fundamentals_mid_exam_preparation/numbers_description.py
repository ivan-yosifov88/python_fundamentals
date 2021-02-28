sequence_of_integers = [int(num) for num in input().split(" ")]

sequence_in_descending_number = sorted(sequence_of_integers, reverse=True)

average_sum_of_sequence = sum(sequence_of_integers) / len(sequence_of_integers)

top_five_numbers = []

counter = 0
for number in sequence_in_descending_number:
    if number > average_sum_of_sequence:
        counter += 1
        top_five_numbers.append(number)
        if counter == 5:
            break
if len(top_five_numbers) == 0:
    print("No")
else:
    print(*top_five_numbers)
