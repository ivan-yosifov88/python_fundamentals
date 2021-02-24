repeating_chars = input()

filter_char = ""
current_char = ""
for char in repeating_chars:
    if char == current_char:
        continue
    else:
        filter_char += char
    current_char = char
print(filter_char)