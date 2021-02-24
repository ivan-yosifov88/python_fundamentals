first_string = input()
second_string = input()

current_string = ""
previous_string = first_string
for iteration in range(len(first_string)):
    for index_second_string in range(0, iteration + 1 ):
        current_string += second_string[index_second_string]
    for index_first_string in range(iteration + 1, len(first_string)):
        current_string += first_string[index_first_string]
    if not previous_string == current_string:
        print(current_string)
    previous_string = current_string
    current_string = ""