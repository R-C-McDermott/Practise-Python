# Full Tic-Tac-Toe game
def create_board():
    ROW1 = ["|   ","|   ","|    |"]
    ROW2 = ["|   ","|   ","|    |"]
    ROW3 = ["|   ","|   ","|    |"]

    board = [ROW1,ROW2,ROW3]

    # return board
    return board

def draw_board(board):
    UNDER_SCORE = " ---  ---  --- "
    print(UNDER_SCORE)
    print(board[0][0],board[0][1],board[0][2])
    print(UNDER_SCORE)
    print(board[1][0],board[1][1],board[1][2])
    print(UNDER_SCORE)
    print(board[2][0],board[2][1],board[2][2])
    print(UNDER_SCORE)

def update_board_X(board, x, y):
    if y == 2:
        board[x][y] = "| X  |"
    if y != 2:
        board[x][y] = "| X "
    return board

def update_board_O(board, x, y):
    if y == 2:
        board[x][y] = "| O  |"
    if y != 2:
        board[x][y] = "| O "
    return board

# FOR LOGIC BOARD

def player_move_X(board):
    input_user = input("Player X, Please select position to play: (in format: 'row column' from 1-3):\n>")
    pos_x, pos_y = input_user.split(" ", 2)
    pos_x = int(pos_x)-1
    pos_y = int(pos_y)-1
    position = [pos_x, pos_y]
    if board[pos_x][pos_y] == 0:
        board[pos_x][pos_y] = "X"
    return position

def player_move_O(board):
    input_user = input("Player O, please select position to play: (in format: 'row column' from 1-3):\n>")
    pos_x, pos_y = input_user.split(" ", 2)
    pos_x = int(pos_x)-1
    pos_y = int(pos_y)-1
    position = [pos_x, pos_y]
    if board[pos_x][pos_y] == 0:
        board[pos_x][pos_y] = "O"
    return position

def check_winner(game):
    win = False
    while win == False:
        if game[0][0] == game[1][1] == game[2][2] != 0:
            player = game[0][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][2] == game[1][1] == game[2][0] != 0:
            player = game[0][2]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][0] == game[0][1] == game[0][2] != 0:
            player = game[0][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[1][0] == game[1][1] == game[1][2] != 0:
            player = game[1][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[2][0] == game[2][1] == game[2][2] != 0:
            player = game[2][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][0] == game[1][0] == game[2][0] != 0:
            player = game[0][0]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][1] == game[1][1] == game[2][1] != 0:
            player = game[0][1]
            win = True
            print(f"Player {player} wins!")
            return False
        if game[0][2] == game[1][2] == game[2][2] != 0:
            player = game[0][2]
            win = True
            print(f"Player {player} wins!")
            return False
        if any(0 in gm for gm in game) == False:
            print("It's a draw!")
            return False
        else:
            return True
            break


def main():
    board = create_board()
    draw_board(board)
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    play = True
    while play == True:
        pos_play_X = player_move_X(game)
        print(game[pos_play_X[0]][pos_play_X[1]])
        if game[pos_play_X[0]][pos_play_X[1]] != "O":
            board = update_board_X(board, pos_play_X[0], pos_play_X[1])
        else:
            print("Space already occupied... Please try again:")
            pos_play_X = player_move_O(game)
            board = update_board_O(board, pos_play_X[0], pos_play_X[1])
        draw_board(board)
        #print(game)
        play = check_winner(game)
        if play == False:
            break
        pos_play_O = player_move_O(game)
        if game[pos_play_O[0]][pos_play_O[1]] != "X":
            board = update_board_O(board, pos_play_O[0], pos_play_O[1])
        else:
            print("Space already occupied... Please try again:")
            pos_play_O = player_move_O(game)
            board = update_board_O(board, pos_play_O[0], pos_play_O[1])
        draw_board(board)
        #print(game)
        play = check_winner(game)
        if play == False:
            break


if __name__ == '__main__':
    main()
