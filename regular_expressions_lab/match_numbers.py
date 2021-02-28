import re

number_sequence = input()
pattern = r"(^|(?<=\s))-?\d+(.\d+)?($|(?=\s))"

matched_numbers = re.finditer(pattern, number_sequence)

for number in matched_numbers:
    print(number.group(), end= " ")