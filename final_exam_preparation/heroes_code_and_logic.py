def cast_spell(heroes_dict, spell):
    hero, mp_needed, spell_name = spell
    mp_needed = int(mp_needed)
    if hero in heroes_dict:
        if heroes_dict[hero]["mp"] >= mp_needed:
            heroes_dict[hero]["mp"] -= mp_needed
            mp_points_left = heroes_dict[hero]["mp"]
            print(f"{hero} has successfully cast {spell_name} and now has {mp_points_left} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    return heroes_dict


def take_damage(heroes_dict, attack):
    hero, damage, attacker = attack
    damage = int(damage)
    if hero in heroes_dict:
        heroes_dict[hero]["hp"] -= damage
        if heroes_dict[hero]["hp"] > 0:
            hp_left = heroes_dict[hero]["hp"]
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {hp_left} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            heroes_dict.pop(hero)
    return heroes_dict


def recharge(heroes_dict, recovery):
    hero, amount = recovery
    amount = int(amount)
    if hero in heroes_dict:
        if heroes_dict[hero]["mp"] + amount > 200:
            amount_recovered = 200 - heroes_dict[hero]["mp"]
            heroes_dict[hero]["mp"] = 200
        else:
            amount_recovered = amount
            heroes_dict[hero]["mp"] += amount
        print(f"{hero} recharged for {amount_recovered} MP!")
    return heroes_dict


def heal(heroes_dict, hp_heal):
    hero, amount = hp_heal
    amount = int(amount)
    if heroes_dict[hero]["hp"] + amount > 100:
        amount_recovered = 100 - heroes_dict[hero]["hp"]
        heroes_dict[hero]["hp"] = 100
    else:
        amount_recovered = amount
        heroes_dict[hero]["hp"] += amount
    print(f"{hero} healed for {amount_recovered} HP!")
    return heroes_dict


number_of_heroes = int(input())

heroes = {}
for _ in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"hp": int(hit_points), "mp": int(mana_points)}

data = input()

while not data == "End":
    command = data.split(" - ")[0]
    if command == "CastSpell":
        new_command = data.split(" - ")[1:]
        cast_spell(heroes, new_command)
    elif command == "TakeDamage":
        new_command = data.split(" - ")[1:]
        take_damage(heroes, new_command)
    elif command == "Recharge":
        new_command = data.split(" - ")[1:]
        recharge(heroes, new_command)
    elif command == "Heal":
        new_command = data.split(" - ")[1:]
        heal(heroes, new_command)

    data = input()
if heroes:
    sorted_heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1]["hp"], x[0])))

    for name in sorted_heroes:
        print(name)
        print(f"  HP: {sorted_heroes[name]['hp']}")
        print(f"  MP: {sorted_heroes[name]['mp']}")


