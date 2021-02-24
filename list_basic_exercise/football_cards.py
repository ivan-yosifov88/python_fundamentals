football_cards = input().split()
team_a_counter = 11
team_b_counter = 11
football_cards_list = []
is_game_break = False
for cards in set(football_cards):
    team_name, player_number = cards.split("-")
    if team_name == "A":
        team_a_counter -= 1
    elif team_name == "B":
        team_b_counter -= 1
    if team_a_counter < 7 or team_b_counter < 7:
        is_game_break = True
        break
print(f"Team A - {team_a_counter}; Team B - {team_b_counter}")
if is_game_break:
    print("Game was terminated")