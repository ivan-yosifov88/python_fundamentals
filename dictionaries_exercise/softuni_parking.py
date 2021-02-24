def register_command(parking_dict, name, plate_number):
    if name not in parking_dict:
        parking_dict[name] = plate_number
        print(f"{name} registered {plate_number} successfully")
    else:
        # for plate in parking_dict.values():
        #     if plate == plate_number:
        print(f"ERROR: already registered with plate number {parking_dict[name]}")
    return parking_dict


def unregister_command(parking_dict, name):
    if name not in parking_dict:
        print(f"ERROR: user {name} not found")
    else:
        print(f"{name} unregistered successfully")
        parking_dict.pop(name)
    return parking_dict


number_of_commands = int(input())

parking_zone = {}
for commands in range(number_of_commands):
    data = input().split()
    new_command = data[0]
    if new_command == "register":
        username = data[1]
        license_plate_number = data[2]
        register_command(parking_zone, username, license_plate_number)

    elif new_command == "unregister":
        username = data[1]
        unregister_command(parking_zone, username)

for user, plate in parking_zone.items():
    print(f"{user} => {plate}")
