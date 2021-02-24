number_of_students = int(input())

students_grades = {}
for students in range(number_of_students):
    student_name = input()
    grade = float(input())
    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(grade)

for student, grade in students_grades.items():
    average_grade = sum(grade) / len(grade)
    students_grades[student] = average_grade

sorted_students_grades = sorted(students_grades.items(), key=lambda x: x[1], reverse=True)
for name, final_grade in sorted_students_grades:
    if final_grade >= 4.5:
        print(f"{name} -> {final_grade:.2f}")
