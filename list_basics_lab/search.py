number_of_rows = int(input())
key_word = input()
new_list = []
filter_list = []
for rows in range(number_of_rows):
    new_word = input()
    new_list.append(new_word)
    if key_word in new_word:
        filter_list.append(new_word)
print(new_list)
print(filter_list)

