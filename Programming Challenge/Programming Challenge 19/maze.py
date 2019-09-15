######## COLUMN IS HORIZONTAL ROW IS VERTICAL

import random

infile = open("MAZE.txt", "r")

maze = [[char for char in line.strip("\n")] for line in infile]


def DisplayMaze(maze):
    for row in maze:
        for column in row:
            print(f"{column} ", end="")
        print()
    print()


def ClearMaze(maze):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == "P":
                maze[row][column] = "."


def SetRandomPrize(maze):
    posX = random.randint(0, 9)
    posY = random.randint(0, 10)
    while maze[posY][posX] == "X" or maze[posY][posX] == "O":
        posX = random.randint(0, 9)
        posY = random.randint(0, 10)
    maze[posY][posX] = "P"


def PrintDirection():
    print("Enter U to move up")
    print("Enter D to move down")
    print("Enter L to move left")
    print("Enter R to move right")
    print("Enter '' to continue with previous move")
    print()


def GetPlayerPosition(maze):
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == "O":
                return [row, column]


def CheckForWin(maze):
    count = 0
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == "P":
                count += 1
    if count == 0:
        print("Player has reached the prize")
        return True
    else:
        return False


def CheckValidMove(maze, direction):
    playerMoveY, playerMoveX = GetPlayerPosition(maze)
    if direction == "U":
        if maze[playerMoveY - 1][playerMoveX] == "X":
            return False

        else:
            return True
    elif direction == "D":
        if maze[playerMoveY + 1][playerMoveX] == "X":
            return False

        else:
            return True
    elif direction == "L":
        if maze[playerMoveY][playerMoveX - 1] == "X":
            return False

        else:
            return True
    elif direction == "R":
        if maze[playerMoveY][playerMoveX + 1] == "X":
            return False
        else:
            return True


##    else:
##        if maze[playerMoveY][playerMoveX] == 'X':
##            return False
##        elif maze[playerMoveY][playerMoveX] == 'P':
##            pass
##        else:
##            return True


def GetDirection(maze):
    global LastMove
    PrintDirection()
    userDirection = input("Enter a choice:")
    if userDirection.upper() == "U":
        if CheckValidMove(maze, "U"):
            playerMoveY, playerMoveX = GetPlayerPosition(maze)
            maze[playerMoveY - 1][playerMoveX] = "O"
            maze[playerMoveY][playerMoveX] = "."
        LastMove = "U"

    elif userDirection.upper() == "D":
        if CheckValidMove(maze, "D"):
            playerMoveY, playerMoveX = GetPlayerPosition(maze)
            maze[playerMoveY + 1][playerMoveX] = "O"
            maze[playerMoveY][playerMoveX] = "."
        LastMove = "D"
    elif userDirection.upper() == "L":
        if CheckValidMove(maze, "L"):
            playerMoveY, playerMoveX = GetPlayerPosition(maze)
            maze[playerMoveY][playerMoveX - 1] = "O"
            maze[playerMoveY][playerMoveX] = "."
        LastMove = "L"
    elif userDirection.upper() == "R":
        if CheckValidMove(maze, "R"):
            playerMoveY, playerMoveX = GetPlayerPosition(maze)
            maze[playerMoveY][playerMoveX + 1] = "O"
            maze[playerMoveY][playerMoveX] = "."
        LastMove = "R"
    else:
        if LastMove != "":
            if CheckValidMove(maze, LastMove):
                playerMoveY, playerMoveX = GetPlayerPosition(maze)
                if LastMove == "U":
                    maze[playerMoveY - 1][playerMoveX] = "O"
                    maze[playerMoveY][playerMoveX] = "."

                elif LastMove == "D":
                    maze[playerMoveY + 1][playerMoveX] = "O"
                    maze[playerMoveY][playerMoveX] = "."

                elif LastMove == "L":
                    maze[playerMoveY][playerMoveX + 1] = "O"
                    maze[playerMoveY][playerMoveX] = "."

                elif LastMove == "R":
                    maze[playerMoveY][playerMoveX + 1] = "O"
                    maze[playerMoveY][playerMoveX] = "."


def main():
    ClearMaze(maze)
    SetRandomPrize(maze)
    DisplayMaze(maze)
    global LastMove
    while True:
        if CheckForWin(maze) != True:
            GetDirection(maze)
            DisplayMaze(maze)
        else:
            break


main()
infile.close()
