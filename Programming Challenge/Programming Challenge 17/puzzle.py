# Task 1
'''

Program design

Top-down design: 2 modules are used - InitializeBoard andd OutputBoard.
Data structure: 4x4 2-d array
Implemented as a list of 4 lists
Each of integer 1,2,3,4 in each row
and once in each colomn and in each quad
returns the board as an array
Procedure OutputBoard
and prints out the array.

'''
# Task 2


def InitializeBoard():
    Board = [[4, 3, 2, 1],
             [1, 2, 4, 3],
             [3, 4, 1, 2],
             [2, 1, 3, 4]]
    return Board


def OutputBoard(board):
    for row in range(4):
        for col in range(4):
            print(board[row][col], end='')

        print()


def transform1(board):
    import random
    row = random.choice(['top', 'bottom'])
    if row == 'top':
        temp = board[0]
        board[0] = board[1]
        board[1] = temp

    else:
        temp = board[2]
        board[2] = board[3]
        board[3] = temp
    return board


def transform2(board):
    import random
    col = random.choice(['left', 'right'])
    if col == 'left':
        for row in range(4):
            temp = board[row][0]
            board[row][0] = board[row][1]
            board[row][1] = temp
    else:
        for row in range(4):
            temp = board[row][2]
            board[row][2] = board[row][3]
            board[row][3] = temp
    return board


def transform3(board):
    temp1 = board[0]
    temp2 = board[1]
    board[0] = board[2]
    board[1] = board[3]
    board[2] = temp1
    board[3] = temp2
    return board


def transform4(board):
    for row in range(4):
        temp1 = board[row][0]
        temp2 = board[row][1]
        board[row][0] = board[row][2]
        board[row][1] = board[row][3]
        board[row][2] = temp1
        board[row][3] = temp2
    return board


def SelectTransformation():
    import random
    choice1 = random.randint(1, 4)
    choice2 = random.randint(1, 4)
    while choice1 == choice2:
        choice2 = random.randint(1, 4)

    return choice1, choice2


def main():
    sudoku = InitializeBoard()
    print("Before Transformation:")
    OutputBoard(sudoku)
    choices = SelectTransformation()
    if choices[0] == 1:
        print("Transformation 1: Swaps two rows in the same quadrants")
        OutputBoard(transform1(sudoku))
    elif choices[0] == 2:
        print("Transformation 2: Swap the left and right quadrant columns entirely")
        OutputBoard(transform2(sudoku))
    elif choices[0] == 3:
        print("Transformation 3: Swaps the top and bottom quadrant rows entirely")
        OutputBoard(transform3(sudoku))
    elif choices[0] == 4:
        print("Transformation 4: Swaps the left and right quadrant columns entirely")
        OutputBoard(transform4(sudoku))
    if choices[1] == 1:
        print("Transformation 1: Swaps two rows in the same quadrants")
        OutputBoard(transform1(sudoku))
    elif choices[1] == 2:
        print("Transformation 2: Swap the left and right quadrant columns entirely")
        OutputBoard(transform2(sudoku))
    elif choices[1] == 3:
        print("Transformation 3: Swaps the top and bottom quadrant rows entirely")
        OutputBoard(transform3(sudoku))
    elif choices[1] == 4:
        print("Transformation 4: Swaps the left and right quadrant columns entirely")
        OutputBoard(transform4(sudoku))


main()
