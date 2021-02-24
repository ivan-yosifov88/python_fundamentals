energy = int(input())
count_of_battles_won = 0
is_won_all_battles = True

command = input()
while not command == "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        count_of_battles_won += 1
    else:
        print(f"Not enough energy! Game ends with {count_of_battles_won} won battles and {energy} energy")
        is_won_all_battles = False
        break
    if count_of_battles_won % 3 == 0:
        energy += count_of_battles_won

    command = input()

if is_won_all_battles:
    print(f"Won battles: {count_of_battles_won}. Energy left: {energy}" )

