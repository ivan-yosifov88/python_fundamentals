line_of_numbers = input().split()
text = list(input())

new_word = ""
for numbers in line_of_numbers:
    sum_numbers = 0
    for number in numbers:
        sum_numbers += int(number)
    if sum_numbers > len(text):
        index = abs(sum_numbers - len(text))
    else:
        index = sum_numbers
    new_word += text.pop(index)
print(new_word)