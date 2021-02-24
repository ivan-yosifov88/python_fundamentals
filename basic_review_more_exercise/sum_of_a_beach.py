word_given = input()
word_lower = word_given.lower()
word_for_check = ["sand", "water", "fish", "sun"]
counter = 0
for iteration in range(len(word_for_check)):
    counter += word_lower.count(word_for_check[iteration])
print(counter)
