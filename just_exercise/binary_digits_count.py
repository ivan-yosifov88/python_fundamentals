number = int(input())
leftover = int(input())
counter = 0
binary = []
while not number == 0:

    result = number % 2
    binary.append(result)
    if result == leftover:
        counter += 1
    number //= 2


print(counter)
binary.reverse()
print("".join(str(element) for element in binary))