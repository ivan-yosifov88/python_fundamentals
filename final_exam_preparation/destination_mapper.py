import re

places_on_map = input()

pattern = r"(/|=)(?P<name>[A-Z]([a-zA-Z]){2,})\1"
# Ines pattern with positive lookahead and lookbehind
# (?<=(/|\=))[A-Z][a-zA-Z]{2,}(?=\1) and finditer and group() this is better solution!

result = re.finditer(pattern, places_on_map)

travel_points = 0
destinations = []
for place in result:
    destinations.append(place.group('name'))
    travel_points += len(place.group("name"))

print(f"Destinations: {', '.join(destinations)}")
# if destinations:
#     print(', '.join(destinations))
print(f"Travel Points: {travel_points}")
