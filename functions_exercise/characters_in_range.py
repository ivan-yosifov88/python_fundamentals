def char_range(a, b):
    chars = ""
    char_a = ord(a)
    char_b = ord(b)
    for char in range(char_a + 1, char_b):
        print(chr(char), end=" ")
    return chars


first_char = input()
second_char = input()

char_range(first_char, second_char)