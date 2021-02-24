students_count = int(input())
course_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_count_attendances = 0
for students in range(students_count):
    count_attendances = int(input())
    total_bonus = count_attendances / course_lectures * (additional_bonus + 5)
    if max_bonus < total_bonus:
        max_bonus = total_bonus
        max_count_attendances = count_attendances
# bonus_list = [int(input()) for students in range(students_count)]
# max_count_attendances = max(bonus_list)
# max_bonus = max_count_attendances / course_lectures * (additional_bonus + 5)

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_count_attendances} lectures.")