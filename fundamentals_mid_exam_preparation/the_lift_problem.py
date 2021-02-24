people_wait_for_lift = int(input())
current_state_of_the_lift = [int(num) for num in input().split(" ")]

for i in range(len(current_state_of_the_lift)):
    people_in_wagon = 4 - current_state_of_the_lift[i]
    if people_wait_for_lift > people_in_wagon:
        people_wait_for_lift -= people_in_wagon
        current_state_of_the_lift[i] += people_in_wagon
    else:
        current_state_of_the_lift[i] += people_wait_for_lift
        people_wait_for_lift -= current_state_of_the_lift[i]
    if people_wait_for_lift == 0:
        break

# if not current_state_of_the_lift.count(4) == len(current_state_of_the_lift) and people_wait_for_lift == 0:
#     print("The lift has empty spots!")
#     print(*current_state_of_the_lift)
# elif people_wait_for_lift > 0:
#     print(f"There isn't enough space! {people_wait_for_lift} people in a queue!")
#     print(*current_state_of_the_lift)
# else:
#     print(*current_state_of_the_lift)
if not current_state_of_the_lift.count(4) == len(current_state_of_the_lift) and people_wait_for_lift == 0:
    print("The lift has empty spots!")
    print(*current_state_of_the_lift)
elif people_wait_for_lift > 0 and current_state_of_the_lift.count(4) == len(current_state_of_the_lift):
    print(f"There isn't enough space! {people_wait_for_lift} people in a queue!")
    print(*current_state_of_the_lift)
else:
    print(*current_state_of_the_lift)