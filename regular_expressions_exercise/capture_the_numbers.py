import re

line_of_symbols = input()
pattern = r'\d+'
while line_of_symbols:
    numbers = re.findall(pattern, line_of_symbols)
    if numbers:
        print(*numbers, end=" ")
    line_of_symbols = input()
