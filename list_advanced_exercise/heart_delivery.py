number_of_hearts = [int(el) for el in input().split("@")]
command = input()
index = 0
while not command == "Love!":
    value = int(command.split()[1])
    index += value
    if index >= len(number_of_hearts):
        index = 0
    if number_of_hearts[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        number_of_hearts[index] -= 2
        if number_of_hearts[index] == 0:
            print(f"Place {index} has Valentine's day.")

    command = input()
print(f"Cupid's last position was {index}.")
if number_of_hearts.count(0) == len(number_of_hearts):
    print("Mission was successful.")
else:
    number_of_fails = [nums for nums in number_of_hearts if not nums == 0]
    print(f"Cupid has failed {len(number_of_fails)} places.")


