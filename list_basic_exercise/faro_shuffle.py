cards = input().split()
number_of_shuffles = int(input())
half_part_of_cards = len(cards) // 2

for iteration in range(number_of_shuffles):
    new_list = []
    for index in range(half_part_of_cards):
        first_cart = cards[index]
        second_card = cards[index + half_part_of_cards]

        new_list.append(first_cart)
        new_list.append(second_card)
    cards = new_list

print(new_list)

