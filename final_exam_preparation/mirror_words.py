import re

symbol_line = input()

pattern_words = r"(@|#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"

result = re.findall(pattern_words, symbol_line)

if not result:
    print("No word pairs found!")
else:
    print(f"{len(result)} word pairs found!")

if result:
    mirror_words = []
    for line in result:
        first_word = line[1]
        second_word = line[2]
        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
    if mirror_words:
        print("The mirror words are:")
        print(', '.join(mirror_words))
    else:
        print("No mirror words!")

else:
    print("No mirror words!")
