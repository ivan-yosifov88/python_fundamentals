sequence_of_words = [element.lower() for element in input().split()]

elements = {}

for key in sequence_of_words:
    if key not in elements:
        elements[key] = 0
    elements[key] += 1

for key in elements.keys():
    if elements[key] % 2 == 1:
        # for key, value in elements.items()
        # if value % 2 != 0:
        print(key, end=" ")
