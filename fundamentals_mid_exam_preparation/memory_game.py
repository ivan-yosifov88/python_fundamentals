sequence_of_elements = input().rstrip()
sequence_of_elements = sequence_of_elements.split()
number_of_moves = 0
command = input()
is_player_win = False
while not command == "end":
    command = command.rstrip()
    index_1, index_2 = command.split(" ")
    index_1 = int(index_1)
    index_2 = int(index_2)
    number_of_moves += 1
    border = -1 < (index_1 or index_2) < len(sequence_of_elements)
    if not border or index_1 == index_2:
        sequence_of_elements.insert(len(sequence_of_elements) // 2, "-" + str(number_of_moves) + "a") , sequence_of_elements.insert(len(sequence_of_elements) // 2, "-" + str(number_of_moves) + "a")
        print("Invalid input! Adding additional elements to the board")
    elif sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        element = sequence_of_elements[index_1]
        if index_2 > index_1:
            sequence_of_elements.pop(index_2)
            sequence_of_elements.pop(index_1)
        else:
            sequence_of_elements.pop(index_1)
            sequence_of_elements.pop(index_2)
        print(f"Congrats! You have found matching elements - {element}!")
    elif not sequence_of_elements[index_1] == sequence_of_elements[index_2]:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {number_of_moves} turns!")
        is_player_win = True
        break
    command = input()
if not is_player_win:
    print("Sorry you lose :(")
    print(*sequence_of_elements)
