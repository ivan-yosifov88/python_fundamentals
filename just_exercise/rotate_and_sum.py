number_sequence = [int(number) for number in input().split()]
number_of_rotations = int(input())

current_sequence = [0] * len(number_sequence)

for iterations in range(number_of_rotations):
    element = number_sequence.pop(-1)
    number_sequence.insert(0, element)
    for i in range(len(number_sequence)):
        current_sequence[i] += number_sequence[i]

print(*current_sequence)