import re

text_string = input()

pattern = r"(#|\|)(?P<name>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"

result = re.finditer(pattern, text_string)

total_calories = 0

food = []

for r in result:
    food_item = r.groupdict()
    total_calories += int(r['calories'])
    food.append(food_item)
print(f"You have food to last you for: {total_calories//2000} days!")

for i in food:
    print(f"Item: {i['name']}, Best before: {i['date']}, Nutrition: {i['calories']}")
