def add_user_command(force_dict, side_to_join, user_to_join):
    for side, user in force_dict.items():
        if user_to_join in user:
            return force_dict
    if side_to_join not in force_dict:
        force_dict[side_to_join] = []
    force_dict[side_to_join].append(user_to_join)
    return force_dict


def change_or_add_user_command(force_dict_to_add, side, user_to_add):
    for sides, users in force_dict_to_add.items():
        if user_to_add in users:
            users.remove(user_to_add)
    add_user_command(force_dict_to_add, side, user_to_add)
    print(f"{user} joins the {side} side!")
    return force_dict_to_add


command = input()

force_side = {}
while not command == "Lumpawaroo":
    if len(command.split(" | ")) > 1:
        force, user = command.split(" | ")
        force_side = add_user_command(force_side, force, user)

    elif len(command.split(" -> ")) > 1:
        user, force = command.split(" -> ")
        force_side = change_or_add_user_command(force_side, force, user)

    command = input()

sorted_force_side = sorted(force_side.items(), key=lambda x: (-len(x[1]), x[0]))
for side_of_force, members in sorted_force_side:
    if len(members) > 0:
        print(f"Side: {side_of_force}, Members: {len(members)}")
        sorted_members = sorted(members)
        for member in sorted_members:
            print(f"! {member}")

