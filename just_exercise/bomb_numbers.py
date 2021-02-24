line_of_numbers = list(map(int, input().split()))
special_bomb_number, power = input().split()
special_bomb_number = int(special_bomb_number)
power = int(power)

index = 0
while index < len(line_of_numbers):
    if line_of_numbers[index] == int(special_bomb_number):
        first_part = index - power
        second_part = index + power + 1
        if first_part > 0 and second_part < len(line_of_numbers):
            line_of_numbers = line_of_numbers[:first_part] + line_of_numbers[second_part:]
            index = 0
            continue
        elif first_part <= 0 and second_part < len(line_of_numbers):
            line_of_numbers = line_of_numbers[second_part:]
            index = 0
            continue
        elif first_part > 0 and second_part >= len(line_of_numbers):
            line_of_numbers = line_of_numbers[:first_part]
            index = 0
            continue
        else:
            line_of_numbers.clear()
    index += 1
print(sum(line_of_numbers))