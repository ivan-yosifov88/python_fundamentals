from math import ceil

number_of_peoples = int(input())
capacity = int(input())
courses = ceil(number_of_peoples / capacity)
print(courses)