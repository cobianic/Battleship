from random import randint

board = []

# Creating the board
for x in range(5):
    board.append(["O"] * 5)


# Adding spaces between dots
def print_board(board):
    for row in board:
        print(" ".join(row))

print("Turn 1")
print_board(board)


# Creating the ship
def random_row(board):
    return randint(1, len(board))


def random_col(board):
    return randint(1, len(board[0]))


ship_row = random_row(board)
ship_col = random_col(board)
# Debug coordinates
print(ship_row)
print(ship_col)
# User input
for turn in range(1, 5, 1):
    guess_row = str(input("Guess Row: "))
    guess_col = str(input("Guess Col: "))

    while not guess_row.isdigit():
        print("Please use digits")
        guess_row = input("Guess Row: ")

    while not guess_col.isdigit():
        print("Please use digits")
        guess_col = input("Guess Col: ")

    if int(guess_row) == int(ship_row) and int(guess_col) == int(ship_col):
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (int(guess_row) < 1 or int(guess_row) > 5) or (int(guess_col) < 1 or int(guess_col) > 5):
            print("Oops, that's not even in the ocean.")
        elif board[int(guess_row)][int(guess_col)] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[int(guess_row)][int(guess_col)] = "X"
    # Turn counting
    print("Turn", turn + 1)
    print_board(board)
    if turn == 4:
        print("Game Over")
        break
