char = input()
new_char = ""
for index in range(len(char)):
    new_char += char[index] * 2
print(new_char)
