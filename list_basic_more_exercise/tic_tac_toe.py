
game_board = []
for _ in range(3):
    row_in_list = []
    for row in input().split(" "):
        row_in_list.append(int(row))
    game_board.append(row_in_list)
#  # rows for player one
if game_board[0].count(1) == 3 or game_board[1].count(1) == 3 or game_board[2].count(1) == 3:
    print("First player won")
#  # rows for for player two
elif game_board[0].count(2) == 3 or game_board[1].count(2) == 3 or game_board[2].count(2) == 3:
    print("Second player won")
# column 0, player one
elif game_board[0][0] == game_board[1][0] == game_board[2][0] == 1:
    print("First player won")
# column 0, player two
elif game_board[0][0] == game_board[1][0] == game_board[2][0] == 2:
    print("Second player won")
# column 1, player one
elif game_board[0][1] == game_board[1][1] == game_board[2][1] == 1:
    print("First player won")
# column 1, player two
elif game_board[0][1] == game_board[1][1] == game_board[2][1] == 2:
    print("Second player won")
# column 2, player one
elif game_board[0][2] == game_board[1][2] == game_board[2][2] == 1:
    print("First player won")
# column 2, player two
elif game_board[0][2] == game_board[1][2] == game_board[2][2] == 2:
    print("Second player won")
# first diagonal player one
elif game_board[0][0] == game_board[1][1] == game_board[2][2] == 1:
    print("First player won")
# first diagonal player two
elif game_board[0][0] == game_board[1][1] == game_board[2][2] == 2:
    print("Second player won")
# second diagonal player one
elif game_board[0][2] == game_board[1][1] == game_board[2][0] == 1:
    print("First player won")
# second diagonal player two
elif game_board[0][2] == game_board[1][1] == game_board[2][0] == 2:
    print("Second player won")
else:
    print("Draw!")
