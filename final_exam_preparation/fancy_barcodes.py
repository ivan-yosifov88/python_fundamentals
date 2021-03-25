import re

pattern = r"@#+[A-Z]([a-zA-Z0-9]){4,}[A-Z]@#+"

digit_pattern = "(\d+)"

number_of_lines = int(input())

for line in range(number_of_lines):
    line = input()
    if re.match(pattern, line):
        if re.findall(digit_pattern, line):
            current_line = re.findall(digit_pattern, line)
            digit = ""
            for el in current_line:
                digit += el
            print(f"Product group: {digit}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
