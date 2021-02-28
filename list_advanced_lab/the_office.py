employee_happiness = input().split()
happiness_factor = int(input())

employee_happiness_list = list(map(int, employee_happiness))

new_happiness_list = [nums * happiness_factor for nums in employee_happiness_list]

average_score = sum(new_happiness_list) / len(new_happiness_list)

happy_count = 0
for iterations in range(len(new_happiness_list)):
    if new_happiness_list[iterations] >= average_score:
        happy_count += 1

if happy_count >= len(new_happiness_list) // 2:
    print(f"Score: {happy_count}/{len(new_happiness_list)}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{len(new_happiness_list)}. Employees are not happy!")
