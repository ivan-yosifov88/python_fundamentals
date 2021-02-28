key = int(input())
number_of_letters = int(input())
new_word = ""

for letters in range(number_of_letters):
    new_letter = input()
    new_word += chr(ord(new_letter) + key)
print(new_word)