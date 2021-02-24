start_number = int(input())
end_number = int(input())
max_number = 0
for number in range(start_number, end_number + 1):
    if number > 0 and number % start_number == 0 and number <= end_number:
        if max_number < number:
            max_number = number
print(max_number)