number_of_letters = int(input())
sum_of_all_letters = 0
for letters in range(number_of_letters):
    new_letter = input()
    sum_of_all_letters += ord(new_letter)
print(f"The sum equals: {sum_of_all_letters}")
