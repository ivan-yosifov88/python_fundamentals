import re


string_line = input()
variable = []
pattern = r"((?<=^_{1})|(?<=\s_{1}))[0-9a-zA-Z]+(?=\s|\.|$)"
variable_names = re.finditer(pattern, string_line)
for name in variable_names:
    variable.append(name.group())
print(",".join(variable))

