number_of_rooms = int(input())
free_chairs = 0
is_chairs_in_each_room = True
for rooms in range(1, number_of_rooms + 1):
    chairs, taken_chairs = input().split()
    taken_chairs = int(taken_chairs)
    difference = abs(len(chairs) - taken_chairs)
    if len(chairs) >= taken_chairs:
        free_chairs += difference
    else:
        print(f"{difference} more chairs needed in room {rooms}")
        is_chairs_in_each_room = False
if is_chairs_in_each_room:
    print(f"Game On, {free_chairs} free chairs left")