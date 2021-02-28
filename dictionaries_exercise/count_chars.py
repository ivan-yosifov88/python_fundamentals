char_list = [element for element in input() if not element == " "]

char_dictionary = {}

for char in char_list:
    if char not in char_dictionary:
        char_dictionary[char] = 0
    char_dictionary[char] += 1

for char, occurrence in char_dictionary.items():
    print(f"{char} -> {occurrence}")