alphabet_dict = {}
for index in range(1, 27):
    letter = 96 + index
    alphabet_dict[chr(letter)] = int(index)

words_to_manipulate = input().split()

total_sum = 0
for word in words_to_manipulate:
    first_letter = word[:1]
    second_letter = word[-1:]
    number = int(word[1:-1])
    if first_letter.isupper():
        divider = alphabet_dict[first_letter.lower()]
        total_sum += number / divider
    elif first_letter.islower():
        multiplier = alphabet_dict[first_letter]
        total_sum += number * multiplier
    if second_letter.isupper():
        subtract = alphabet_dict[second_letter.lower()]
        total_sum -= subtract
    elif second_letter.islower():
        add = alphabet_dict[second_letter]
        total_sum += add
print(f"{total_sum:.2f}")