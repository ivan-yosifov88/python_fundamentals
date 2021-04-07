import re

pattern = r"!(?P<title>[A-Z][a-z]{2,})!:\[(?P<message>[a-zA-Z]{8,})\]"

number_of_lines = int(input())

for _ in range(number_of_lines):
    message_to_check = input()
    if re.match(pattern, message_to_check):
        message_to_check = re.finditer(pattern, message_to_check)
        for current_message in message_to_check:
            current_message = current_message.groupdict()
            print(f"{current_message['title']}: {' '.join(str(ord(el)) for el in current_message['message'])}")
    else:
        print("The message is invalid")