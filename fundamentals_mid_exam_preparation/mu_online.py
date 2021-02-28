initial_health = 100
initial_bitcoins = 0
dungeons_rooms = input().split("|")


def potion_command(num, health):
    amount = 0
    if health + num < 100:
        health += num
        amount = num
    else:
        amount = 100 - health
        health = 100
    # if initial_health == 100:
    #     amount = 0
    # else:
    #     if initial_health + num > 100:
    #         amount = 100 - initial_health
    #         initial_health = 100
    #     else:
    #         initial_health += num
    #         amount = num
    print(f"You healed for {amount} hp.")
    print(f"Current health: {health} hp.")
    return health


def chest_command(num, bitcoins):
    bitcoins += num
    print(f"You found {num} bitcoins.")
    return bitcoins


def monster_command(num, health, monster_name, room):
    health -= num
    if health > 0:
        print(f"You slayed {monster_name}.")
    else:
        print(f"You died! Killed by {monster_name}.")
        print(f"Best room: {room}")
    return health


is_he_made_it = True
room_number = 1
for room in dungeons_rooms:
    command, value = room.split(" ")
    value = int(value)
    if command == "potion":
        initial_health = potion_command(value, initial_health)
    elif command == "chest":
        initial_bitcoins = chest_command(value, initial_bitcoins)
    else:
        initial_health = monster_command(value, initial_health, command, room_number)
        if initial_health <= 0:
            is_he_made_it = False
            break
    room_number += 1
if is_he_made_it:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")