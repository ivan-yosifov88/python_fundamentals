number_of_rows = int(input())
number_of_open_bracket = 0
number_of_close_bracket = 0
total_of_brackets = 0
for rows in range(number_of_rows):
    new_row = input()
    if new_row == chr(40) or new_row == chr(41):
        total_of_brackets += 1
    if new_row == chr(40):
        number_of_open_bracket += 1
    if number_of_open_bracket - 1 == number_of_close_bracket:
        if new_row == chr(41):
            number_of_close_bracket += 1
if number_of_open_bracket == number_of_close_bracket == int(total_of_brackets / 2):
    print("BALANCED")
else:
    print("UNBALANCED")

