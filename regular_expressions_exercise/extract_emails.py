import re

string_line = input()
pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"


email_validator = re.finditer(pattern, string_line)
for email in email_validator:
    print(email.group())