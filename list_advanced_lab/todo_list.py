command = input()
todo_list = [0] * 10
while not command == "End":
    tokens = command.split("-")
    index = int(tokens[0]) - 1
    task = tokens[1]
    todo_list[index] = task
    command = input()
task_list = []
for tasks in todo_list:
    if tasks != 0:
        task_list.append(tasks)

print(task_list)
