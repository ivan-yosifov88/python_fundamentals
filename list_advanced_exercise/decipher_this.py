secret_message = input().split()

for word in secret_message:
    number = ""
    new_word = []
    for symbols in word:
        if symbols.isnumeric():
            number += symbols
        else:
            new_word += symbols
    new_word[0], new_word[-1] = new_word[-1], new_word[0]
    new_word.insert(0, chr((int(number))))
    print("".join(new_word), end=" ")
