string_line = input()

encrypted_version = ""

for letter in string_line:
    encrypted_version += chr(ord(letter) + 3)
print(encrypted_version)