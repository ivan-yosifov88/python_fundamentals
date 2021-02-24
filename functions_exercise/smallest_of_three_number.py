import sys


def find_smallest(num1, num2, num3):
    smallest_num = sys.maxsize
    if num1 < smallest_num:
        smallest_num = num1
    if num2 < smallest_num:
        smallest_num = num2
    if num3 < smallest_num:
        smallest_num = num3
    return smallest_num


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(find_smallest(first_number, second_number, third_number))

