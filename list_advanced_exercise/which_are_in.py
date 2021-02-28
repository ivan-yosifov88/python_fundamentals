list_of_substrings = input().split(", ")
list_of_strings = input()

new_list = []
for word in list_of_substrings:
    if word in list_of_strings and word not in new_list:
        new_list.append(word)


print(new_list)

