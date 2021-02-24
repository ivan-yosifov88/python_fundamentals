string_line = input()

rage_string = ""
current_string = ""
index = 0
while index < len(string_line):
    symbol = string_line[index]
    if not string_line[index].isdigit():
        current_string += symbol.upper()
        index += 1
    else:
        multiplier = ""
        # # this is slow
        # for num in string_line[index:]:
        #     if num.isdigit():
        #         multiplier += num
        #     else:
        #         break
        while index < len(string_line) and string_line[index].isdigit():
            multiplier += string_line[index]
            index += 1
        current_string *= int(multiplier)
        rage_string += current_string
        current_string = ""

unique_symbols = len(set(rage_string))
print(f"Unique symbols used: {unique_symbols}")
print(rage_string)




