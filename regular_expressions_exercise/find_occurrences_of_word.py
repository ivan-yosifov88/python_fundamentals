import re

text_line = input()
word_to_check = input()
pattern = f"(\\b{word_to_check}\\b)"
word_occurrence = re.findall(pattern, text_line, re.IGNORECASE)
print(len(word_occurrence))
