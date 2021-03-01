cards = input().split(":")

deck = []
data = input()

while not data == "Ready":
    command = data.split()[0]
    if command == "Add":
        card_name = data.split()[1]
        if card_name in cards:
            deck.append(card_name)
        else:
            print("Card not found.")
    elif command == "Insert":
        card_name = data.split()[1]
        index = data.split()[2]
        index = int(index)
        if card_name in cards and 0 <= index <= len(deck):
            deck.insert(index, card_name)
        else:
            print("Error!")
    elif command == "Remove":
        card_name = data.split()[1]
        if card_name in deck:
            deck.remove(card_name)
        else:
            print("Card not found.")
    elif command == "Swap":
        first_card = data.split()[1]
        second_card = data.split()[2]
        first_card_index = deck.index(first_card)
        second_card_index = deck.index(second_card)
        deck[first_card_index], deck[second_card_index] = deck[second_card_index], deck[first_card_index]
    elif command == "Shuffle":
        deck.reverse()
    data = input()
print(*deck)