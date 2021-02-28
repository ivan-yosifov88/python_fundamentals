lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
helmet_repair = 0
sword_repair = 0
shield_repair = 0
armor_repair = 0
for lost in range(1, lost_fights_count + 1):
    if lost % 2 == 0:
        helmet_repair += 1
    if lost % 3 == 0:
        sword_repair += 1
    if lost % 2 == 0 and lost % 3 == 0:
        shield_repair += 1
        if shield_repair % 2 == 0:
            armor_repair += 1
expenses = helmet_price * helmet_repair + sword_price * sword_repair + shield_price * shield_repair + armor_price * armor_repair
print(f"Gladiator expenses: {expenses:.2f} aureus")