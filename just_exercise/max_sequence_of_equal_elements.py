number_sequence = [int(number) for number in input().split()]
final_sequence = []
for index in range(len(number_sequence)):
    max_sequence = [number_sequence[index]]
    while index + 1 < len(number_sequence):
        index += 1
        if number_sequence[index] in max_sequence:
            max_sequence.append(number_sequence[index])
        else:
            break
    if len(max_sequence) > len(final_sequence):
        final_sequence = max_sequence

print(*final_sequence)