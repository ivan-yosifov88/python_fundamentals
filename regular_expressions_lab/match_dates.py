import re

date = input()
pattern = r"\b(?P<Day>\d{2})([\.|/|-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"

dates = re.finditer(pattern, date)

for date in dates:
    print(f"Day: {date.group('Day')}, Month: {date.group('Month')}, Year: {date.group('Year')}")