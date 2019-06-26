# Tic-Tac-Toe
# The grid is represented using a 2D array of size 3 x 3
# Characters used are:
# ' ' (space) to represent no mark
# 'X' to represent X
# 'O' to represent O
#
# Initial grid value is set to space for all the space in the 3 x 3 grid
# There are 10 blank spaces declared
# This is to simplify the array indexing by referring to each space
# Using the position as shown above.
# Hence the first index 0 is ignored

board = [" " for x in range(10)]


def displayInstructions():
    print("Use the numbers indicated in each space to make your mark")
    print("   |   |   ")
    print(" 7 | 8 | 9 ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" 4 | 5 | 6 ")
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" 1 | 2 | 3 ")
    print("   |   |   ")
    print("\n-------------------------------------------------------\n")


def displayBoard(board):
    """displayBoard This function prints out the board that it was passed.

    Arguments:
        board {list} -- Tic Tac Toe board

    """
    print("The Game Board: ")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")
    print("---------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("---------")
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")


def getPlayerMove(board, player):
    # Let the player type his move
    move = " "
    while True:
        print("What is {0} next move? (1-9)".format(player))
        move = input()
        if move.isdigit():
            if int(move) > 0 and int(move) < 10:
                if board[int(move)] == " ":
                    print(board[int(move)])
                    return int(move)
                else:
                    print("Sorry this space is occupied")
                    continue
            else:
                print("Please type a number within the range!")
                continue
        else:
            print("Please enter a digit")
            continue


def checkWin(board, letter):
    return (
        # Horizontal Top
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        # Horizontal Middle
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        # Horizontal Bottom
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        # Vertical Left
        (board[7] == letter and board[4] == letter and board[1] == letter) or
        # Vertical Middle
        (board[8] == letter and board[5] == letter and board[2] == letter) or
        # Vertical Right
        (board[9] == letter and board[6] == letter and board[3] == letter) or
        # Diagonal
        (board[7] == letter and board[5] == letter and board[3] == letter) or
        # Diagonal
        (board[9] == letter and board[5] == letter and board[1] == letter)
    )


def isBoardFull(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def main():
    print("Welcome to Tic Tac Toe")
    displayInstructions()
    displayBoard(board)

    print("Player 1 will use X")
    print("Player 2 will use O.")
    print("Which player will go first [1/2]?", end=" ")
    turn = eval(input())

    gameIsPlaying = True
    while gameIsPlaying:
        if turn == 1:
            print("Player 1's turn")
            displayBoard(board)
            move = getPlayerMove(board, 'player 1')
            board[move] = 'X'

            if checkWin(board, 'X'):
                displayBoard(board)
                print('Player 1 won!')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    displayBoard(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = 2
        else:
            print("Player 2's turn")
            displayBoard(board)
            move = getPlayerMove(board, 'player 2')
            board[move] = 'O'

            if checkWin(board, 'O'):
                displayBoard(board)
                print('Player 2 won!')
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    displayBoard(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = 1


main()
