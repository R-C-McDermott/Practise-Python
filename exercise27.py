# Exercise 27

board = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]


def player_move_X(board):
    input_user = input("Please select position to play: (in format: 'row column' from 1-3):\n>")
    pos_x, pos_y = input_user.split(" ", 2)
    pos_x = int(pos_x)-1
    pos_y = int(pos_y)-1
    print(pos_x)
    print(pos_y)
    board[pos_x][pos_y] = "X"
    print(board)

def player_move_O(board):
    input_user = input("Please select position to play: (in format: 'row column' from 1-3):\n>")
    pos_x, pos_y = input_user.split(" ", 2)
    pos_x = int(pos_x)-1
    pos_y = int(pos_y)-1
    print(pos_x)
    print(pos_y)
    board[pos_x][pos_y] = "O"
    print(board)


def main():
    print(board)
    player_move_X(board)
    player_move_O(board)

if __name__ == '__main__':
    main()
