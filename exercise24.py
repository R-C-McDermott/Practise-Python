# Exercise 24

# Tic, tac, toe part 1!

def create_board(rows, columns):
    board = ""

    # there are 5 rows in a standard tic-tac-toe board
    for i in range(-1,rows*2):
        # switch between printing vertical and horizontal bars
        if i%2 == 0:
            board += "|    " * (columns+1)
        else:
            board += " --- " * columns
        # don't forget to start a new line after each row using "\n"
        board += "\n"

    print(board)

def main():
    create_board(3,3)

if __name__ == '__main__':
    main()
