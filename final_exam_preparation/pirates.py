def plunder_func(targ, town, popul, prof):
    if town in targ:
        print(f"{town} plundered! {prof} gold stolen, {popul} citizens killed.")
        if targ[town][0] - popul == 0 or targ[town][1] - prof == 0:
            print(f"{town} has been wiped off the map!")
            targ.pop(town)
        else:
            targ[town][0] -= popul
            targ[town][1] -= prof
        return targ


def prosper_func(targ, town, prof):
    if prof < 0:
        print("Gold added cannot be a negative number!" )
    else:
        targ[town][1] += prof
        print(f"{prof} gold added to the city treasury. {town} now has {targ[town][1]} gold.")


command = input()

target = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    population = int(population)
    gold = int(gold)
    if city not in target:
        target[city] = []
        target[city].append(population)
        target[city].append(gold)
    else:
        target[city][0] += population
        target[city][1] += gold

    command = input()

data = input()

while not data == "End":
    event = data.split("=>")[0]
    if event == "Plunder":
        town, people, amount_of_gold = data.split("=>")[1:]
        people = int(people)
        amount_of_gold = int(amount_of_gold)
        target = plunder_func(target, town, people, amount_of_gold)
    elif event == "Prosper":
        town, gold = data.split("=>")[1:]
        gold = int(gold)
        prosper_func(target, town, gold)

    data = input()

sorted_targets = dict(sorted(target.items(), key=lambda x:(-x[1][1],x[0])))
print(f"Ahoy, Captain! There are {len(sorted_targets.keys())} wealthy settlements to go to:")
for town in sorted_targets.items():
    print(f"{town[0]} -> Population: {town[1][0]} citizens, Gold: {town[1][1]} kg")




