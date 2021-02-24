list_of_hearts = [int(heart) for heart in input().split("@")]

data = input()

index = 0
while not data == "Love!":
    command, value = data.split(" ")
    value = int(value)
    index += value
    if index >= len(list_of_hearts):
        index = 0
    if list_of_hearts[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        list_of_hearts[index] -= 2
        if list_of_hearts[index] == 0:
            print(f"Place {index} has Valentine's day.")

    data = input()

print(f"Cupid's last position was {index}.")
house_count = [number for number in list_of_hearts if not number == 0]
if len(house_count) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(house_count)} places.")
