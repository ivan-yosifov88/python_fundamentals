number = int(input())
for rows in range(1, number + 1):
    print("*" * rows)
for rows_down in range(rows - 1, 0, - 1):
    print("*" * rows_down)