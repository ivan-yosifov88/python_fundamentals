import re

text = input()
pattern_digits = r"\d"

digits_in_text = re.findall(pattern_digits, text)

digit_multiply_result = 1
for digit in digits_in_text:
    digit_multiply_result *= int(digit)

pattern_emoji = r"(::|\*\*)[A-Z][a-z]{2,}\1"
emoji_in_text = re.finditer(pattern_emoji, text)
emoji_count = len(re.findall(pattern_emoji, text))
print(f"Cool threshold: {digit_multiply_result}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in emoji_in_text:
    result = 0
    for letter in emoji.group()[2:-2]:
        result += ord(letter)
    if result >= digit_multiply_result:
        print(emoji.group())

