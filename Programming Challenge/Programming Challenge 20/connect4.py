def InitialiseBoard():
    Board = [["-" for col in range(7)] for row in range(6)]
    return Board


def SetUpGame():
    GameFinished = False
    ThisPlayer = "O"
    return GameFinished, ThisPlayer


def OutputBoard(Board):
    count = 1
    print("   1  2  3  4  5  6  7")
    for row in Board:
        print(count, end=" ")
        count += 1
        for col in row:
            print(f"{col:^3}", end="")
        print()


def ThisPlayerMakesMove(Board, ThisPlayer):
    player_input = input("Enter a valid column number(1-7): ")
    # Check if the player_input is in between 1 - 7
    while int(player_input) not in range(1, 8):
        print("Please enter another column")
        player_input = input("Enter a valid column number(1-7): ")

    for row in range(len(Board), 0, -1):
        if Board[row - 1][int(player_input) - 1] == "-":
            Board[row - 1][int(player_input) - 1] = ThisPlayer
            break
        if Board[0][int(player_input) - 1] != "-":
            print("Column is full")
            break


def CheckIfThisPlayerHasWon(Board, ThisPlayer):
    for row in range(len(Board)):
        for col in range(len(Board[0]) - 3):
            if (
                Board[row][col] == ThisPlayer
                and Board[row][col + 1] == ThisPlayer
                and Board[row][col + 2] == ThisPlayer
                and Board[row][col + 3] == ThisPlayer
            ):
                return True

    for row in range(len(Board) - 3):
        for col in range(len(Board[0])):
            if (
                Board[row][col] == ThisPlayer
                and Board[row + 1][col] == ThisPlayer
                and Board[row + 2][col] == ThisPlayer
                and Board[row + 3][col] == ThisPlayer
            ):
                return True
    return False


def SwapThisPlayer(ThisPlayer):
    if ThisPlayer == "O":
        ThisPlayer = "X"
    else:
        ThisPlayer = "O"
    return ThisPlayer


def main():
    Board = InitialiseBoard()
    GameFinished, ThisPlayer = SetUpGame()
    OutputBoard(Board)
    while GameFinished == False:
        ThisPlayerMakesMove(Board, ThisPlayer)
        OutputBoard(Board)
        GameFinished = CheckIfThisPlayerHasWon(Board, ThisPlayer)
        if GameFinished == False:
            ThisPlayer = SwapThisPlayer(ThisPlayer)
        else:
            print()
            print(f"Player {ThisPlayer} has won!!!!")


main()
