puzzle1 = [
    [8, 2, 5, 4, 7, 1, 3, 9, 6],
    [1, 9, 4, 3, 2, 6, 5, 7, 8],
    [3, 7, 6, 9, 8, 5, 2, 4, 1],
    [5, 1, 9, 7, 4, 3, 8, 6, 2],
    [6, 3, 2, 5, 9, 8, 4, 1, 7],
    [4, 8, 7, 6, 1, 2, 9, 3, 5],
    [2, 6, 3, 1, 5, 9, 7, 8, 4],
    [9, 4, 8, 2, 6, 7, 1, 5, 3],
    [7, 5, 1, 8, 3, 4, 6, 2, 9],
]

puzzle2 = [
    [2, 4, 8, 3, 9, 5, 7, 1, 6],
    [5, 7, 1, 6, 2, 8, 3, 4, 9],
    [9, 3, 6, 7, 4, 1, 5, 8, 2],
    [6, 8, 2, 5, 3, 9, 1, 7, 4],
    [3, 5, 9, 1, 7, 4, 6, 2, 8],
    [7, 1, 4, 8, 6, 9, 2, 5, 3],
    [8, 6, 3, 4, 1, 7, 2, 9, 5],
    [1, 9, 5, 2, 8, 6, 4, 3, 7],
    [4, 2, 7, 9, 5, 3, 8, 6, 1],
]

puzzle3 = [
    [1, 7, 5, 8, 3, 9, 4, 2, 6],
    [6, 3, 8, 2, 7, 4, 9, 1, 5],
    [4, 2, 9, 6, 5, 1, 3, 7, 8],
    [8, 1, 6, 3, 9, 5, 7, 4, 2],
    [5, 4, 7, 1, 6, 2, 8, 3, 9],
    [2, 9, 3, 4, 7, 8, 6, 5, 1],
    [7, 5, 4, 9, 2, 6, 1, 8, 3],
    [9, 8, 1, 5, 4, 3, 2, 6, 7],
    [3, 6, 2, 7, 1, 5, 8, 9, 4],
]


def displayboard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()


# each row must contain all numbers 1-9
# each col must contain all numbers 1-9
# each quadrant must contain all numbers 1-9


def checkRow(board):
    for i in range(9):
        fullSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if board[i][j] in fullSet:
                fullSet.remove(board[i][j])
        if len(fullSet) != 0:
            return False
    return True


def checkColumn(board):
    for i in range(9):
        fullSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            if board[j][i] in fullSet:
                fullSet.remove(board[j][i])
        if len(fullSet) != 0:
            return False
    return True


##def checkFirstBlock(board):        ##Read this first to understand how to use 2 for-loops to check first block only
##    fullSet = [1,2,3,4,5,6,7,8,9]
##    for i in range(0,3):           #start coordinates
##        for j in range(0,3):       #end coordinates
##            if board[i][j] in fullSet:
##                print(board[i][j])
##                fullSet.remove(board[i][j])
##                print(fullSet)
##    if len(fullSet)==0: return True
##    return False


def checkBlock(board):
    blockIndex = [(0, 3), (3, 6), (6, 9)]  # coordinates of the blocks
    for x in range(3):
        for y in range(3):
            fullSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(blockIndex[x][0], blockIndex[x][1]):  # start coordinates
                for j in range(blockIndex[y][0], blockIndex[y][1]):  # end coordinates
                    if board[i][j] in fullSet:
                        fullSet.remove(board[i][j])
            if len(fullSet) != 0:
                return False
    return True


def checkSudoku(puzzle):
    displayboard(puzzle)
    if checkRow(puzzle):
        rowFlag = True
    else:
        rowFlag = False
    if checkColumn(puzzle):
        colFlag = True
    else:
        colFlag = False
    if checkBlock(puzzle):
        blockFlag = True
    else:
        blockFlag = False
    return rowFlag, colFlag, blockFlag


def main():
    while True:
        option = input("\nChoose one puzzle\n1)puzzle1 \n2)puzzle2 \n3)puzzle3\n>>")
        rowFlag = None
        colFlag = None
        blockFlag = None
        if option == "1":
            rowFlag, colFlag, blockFlag = checkSudoku(puzzle1)
        elif option == "2":
            rowFlag, colFlag, blockFlag = checkSudoku(puzzle2)
        elif option == "3":
            rowFlag, colFlag, blockFlag = checkSudoku(puzzle3)

        # print statements
        if rowFlag:
            print("Row is valid.")
        elif rowFlag is False:
            print("Row is invalid!")
        if colFlag:
            print("Column is valid.")
        elif colFlag is False:
            print("Column is invalid!")
        if blockFlag:
            print("Block is valid.")
        elif blockFlag is False:
            print("Block is invalid!")

        carryOn = input("\nCheck another puzzle? [Y/N] ")
        if carryOn[0].upper() != "Y":
            print("Goodbye!")
            break


main()
