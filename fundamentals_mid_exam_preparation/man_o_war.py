pirate_ship = [int(num)for num in input().split(">")]
war_ship = [int(num)for num in input().split(">")]
maximum_section_health = int(input())
is_win = False

data = input()

while not data == "Retire":
    command = data.split()[0]
    if command == "Fire":
        index = int(data.split()[1])
        damage = int(data.split()[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_win = True
                break
    elif command == "Defend":
        start_index = int(data.split()[1])
        end_index = int(data.split()[2])
        damage = int(data.split()[3])
        if 0 <= start_index < len(pirate_ship) and 0 < end_index + 1 <= len(pirate_ship):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= damage
                if pirate_ship[index] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_win = True
                    break
        if is_win:
            break
    elif command == "Repair":
        index = int(data.split()[1])
        health = int(data.split()[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] >= maximum_section_health:
                pirate_ship[index] = maximum_section_health
    elif command == "Status":
        count = 0
        for element in pirate_ship:
            if element < maximum_section_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    data = input()
if not is_win:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")