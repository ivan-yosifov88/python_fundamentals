event_list = input().split("|")
initial_energy = 100
initial_coins = 100
is_bankrupt = False

for events in event_list:
    event, value = events.split("-")
    value = int(value)
    if event == "rest":
        gained_energy = 0
        if initial_energy + value < 100:
            initial_energy += value
            gained_energy = value
        else:
            gained_energy = 100 - initial_energy
            initial_energy = 100
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif event == "order":
        if initial_energy < 30:
            initial_energy += 50
            print("You had to rest!")
            continue
        initial_coins += value
        initial_energy -= 30
        print(f"You earned {value} coins.")
    else:
        if initial_coins > value:
            initial_coins -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            is_bankrupt = True
            break
if not is_bankrupt:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
# if initial_energy < 30:
#     initial_energy += 50
#     print("You had to rest!")
#     continue
# initial_coins += value
# initial_energy -= 30
# print(f"You earned {value} coins.")
# Защо не работи така !!!!!!!!

# if initial_energy < 30:
#     initial_coins += 50
#     print("You had to rest!")
# else:
#     initial_coins += value
#     print(f"You earned {value} coins.")
#     initial_energy -= 30