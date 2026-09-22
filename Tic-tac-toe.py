board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6] ]
    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True
    return False

def check_draw():
    return " " not in board

current_player = "X"
print("Tic-Tac-Toe")
print("Player X vs Player O")
while True:
    display_board()
    position = int(input("Player " + current_player + ", choose position (1-9): "))
    if position < 1 or position > 9:
        print("Choose a position between 1 and 9.")
        continue
    position = position - 1
    if board[position] != " ":
        print("That position is already occupied.")
        continue
    board[position] = current_player
    if check_winner(current_player):
        display_board()
        print("Player", current_player, "wins!")
        break
    if check_draw():
        display_board()
        print("It's a draw!")
        break
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
