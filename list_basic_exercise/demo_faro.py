deck = input().split()
number_of_shuffles = int(input())
left_half = []
right_half = []

for shuffles in range(number_of_shuffles):
    current_deck = []
    half_of_deck = len(deck) // 2
    left_half = deck[0:half_of_deck]
    right_half = deck[half_of_deck::]
    for cart in range(len(left_half)):
        current_deck.append(left_half[cart])
        current_deck.append(right_half[cart])

    deck = current_deck

print(deck)


