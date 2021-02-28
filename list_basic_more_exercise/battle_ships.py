number_of_rows = int(input())

total_battle_ships = []
for _ in range(number_of_rows):
    battle_ships = [int(number) for number in input().split()]
    total_battle_ships.append(battle_ships)

number_of_attacks = input().split()

destroyed_ships = 0
for attack in number_of_attacks:
    row, column = attack.split("-")
    row = int(row)
    column = int(column)
    total_battle_ships[row][column]
    if not total_battle_ships[row][column] == 0:
        total_battle_ships[row][column] -= 1
        if total_battle_ships[row][column] == 0:
            destroyed_ships += 1

print(destroyed_ships)