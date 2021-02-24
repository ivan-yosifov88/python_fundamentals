word = input()
upper_letters = []
for index in range(len(word)):
    if word[index].isupper():
        upper_letters.append(index)
print(upper_letters)