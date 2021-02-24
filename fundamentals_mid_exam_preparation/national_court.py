first_employee_count = int(input())
second_employee_count = int(input())
third_employee_count = int(input())
count_of_people = int(input())
total_employees_count = first_employee_count + second_employee_count + third_employee_count

hours = 0
while count_of_people > 0:
    count_of_people -= total_employees_count
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")