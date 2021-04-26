# Exercise 26

# Tic Tac Toe win check!

b = [[1, 0, 0],[1, 0, 0],[1, 0, 0]] # Player 1 wins
c = [[1, 2, 0],[1, 0, 2],[1, 2, 0]] # Player 1 wins
d = [[2, 1, 0],[1, 2, 0],[1, 0, 2]] # Player 2 wins
draw = [[2, 1, 0],[0, 2, 1],[1, 2, 0]] # Draw


def check_winner(game):
    win = False
    while win == False:
        if game[0][0] == game[1][1] == game[2][2] != 0:
            player = game[0][0]
            win = True
        if game[0][2] == game[1][1] == game[2][0] != 0:
            player = game[0][2]
            win = True
        if game[0][0] == game[0][1] == game[0][2] != 0:
            player = game[0][0]
            win = True
        if game[1][0] == game[1][1] == game[1][2] != 0:
            player = game[1][0]
            win = True
        if game[2][0] == game[2][1] == game[2][2] != 0:
            player = game[2][0]
            win = True
        if game[0][0] == game[1][0] == game[2][0] != 0:
            player = game[0][0]
            win = True
        if game[0][1] == game[1][1] == game[2][1] != 0:
            player = game[0][1]
            win = True
        if game[0][2] == game[1][2] == game[2][2] != 0:
            player = game[0][2]
            win = True
        if win == True:
            print(f"Player {player} wins!")
        else:
            print("Draw!")
            break

def main():
    check_winner(d)

if __name__ == "__main__":
    main()
