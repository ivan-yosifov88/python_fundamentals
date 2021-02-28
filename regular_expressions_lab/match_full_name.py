import re

data = input()
regex_pattern = r"\b[A-Z][a-z]+ +[A-Z][a-z]+\b"

valid_names = re.findall(regex_pattern, data)

print(*valid_names, sep=" ")