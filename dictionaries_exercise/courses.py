data = input()

course_register = {}
while not data == "end":
    course_name, student_name = data.split(" : ")
    if course_name not in course_register:
        course_register[course_name] = []
    course_register[course_name].append(student_name)

    data = input()

sorted_register = sorted(course_register.items(), key=lambda x: -len(x[1]))
for course, student in sorted_register:
    print(f"{course}: {len(student)}")
    sorted_students = sorted(student)
    for students in sorted_students:
        print(f"-- {students}")