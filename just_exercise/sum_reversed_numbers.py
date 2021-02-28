list_of_numbers = input().split()

result = 0

for number in list_of_numbers:
    number = int(number[::-1])
    result += number

print(result)