def palindrome_validator(list_int):
    for numbers in list_int:
        if numbers == numbers[::-1]:
            print(True)
        else:
            print(False)


list_on_numbers = input().split(", ")

palindrome_validator(list_on_numbers)