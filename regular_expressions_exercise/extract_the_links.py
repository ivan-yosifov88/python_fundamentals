import re

text_to_check = input()
pattern = r"www.[a-zA-Z0-9]+((\-[a-zA-Z0-9]+)?)+(\.[a-z]+)+"
while text_to_check:
    fonded_links = re.finditer(pattern, text_to_check)
    for link in fonded_links:
        print(link.group())
    text_to_check = input()
