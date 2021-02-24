symbol_line = input()

string_line = []
number_line = []

for symbol in symbol_line:
    if symbol.isdigit():
        number_line.append(int(symbol))
    else:
        string_line.append(symbol)

take_list = []
skip_list = []

for i in range(len(number_line)):
    if i % 2 == 0:
        take_list.append(number_line[i])
    else:
        skip_list.append(number_line[i])

index = 0
result_string = []
# while index < len(string_line):
for iterations in range(len(number_line)//2):
    take = take_list[iterations]
    skip = skip_list[iterations]
    result_string.extend(string_line[index:index + take])
    index += take
    index += skip
    if index >= len(string_line):
        break

print("".join(result_string))


