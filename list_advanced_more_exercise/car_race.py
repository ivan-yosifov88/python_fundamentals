line_with_times = input().split()
finish_line = len(line_with_times) // 2
left_racer = line_with_times[:finish_line]
# right_racer = list(reversed(line_with_times[finish_line + 1:]))
right_racer = line_with_times[-1: finish_line:-1]

left_racer_time = 0
right_racer_time = 0
for race in range(finish_line):
    if int(left_racer[race]) == 0:
        left_racer_time *= 0.8
    else:
        left_racer_time += int(left_racer[race])
    if int(right_racer[race]) == 0:
        right_racer_time *= 0.8
    else:
        right_racer_time += int(right_racer[race])

winner = ""
if left_racer_time < right_racer_time:
    winner = "left"
    print(f"The winner is {winner} with total time: {left_racer_time:.1f}")
elif left_racer_time > right_racer_time:
    winner = "right"
    print(f"The winner is {winner} with total time: {right_racer_time:.1f}")