string_line = input()
digit = ""
letter = ""
other_char = ""

for symbol in string_line:
    if symbol.isdigit():
        digit += symbol
    elif symbol.isalpha():
        letter += symbol
    else:
        other_char += symbol
print(digit)
print(letter)
print(other_char)