import random
grid = [['.' for j in range(15)] for i in range(8)]


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print()


def throw_stone(x, y):
    grid[y][x] = 'S'


def spawn_fish():
    fishes = 3
    while fishes > 0:
        x_coor_fish = random.randint(0, 14)
        y_coor_fish = random.randint(0, 7)
        if grid[y_coor_fish][x_coor_fish] == 'F':
            continue
        else:
            grid[y_coor_fish][x_coor_fish] = 'F'
            fishes -= 1


def throw_pellets(x, y):
    if not grid[y][x] == 'F':
        grid[y][x] = 'P'
    else:
        grid[y][x] = 'H'


def main():
    while True:
        x_coor = input("X coordinate <1 to 15>? ")
        y_coor = input("Y coordinate <1 to 8>? ")
        if not x_coor.isdigit() or not y_coor.isdigit():
            print("Wrong value sorry. Try again.. ")
            continue
        else:
            throw_stone(int(x_coor)-1, int(y_coor)-1)
            print_grid(grid)
            break
    spawn_fish()
    index = 2
    while True:
        x_coor = input("X coordinate <1 to 15>? ")
        y_coor = input("Y coordinate <1 to 8>? ")
        if not x_coor.isdigit() or not y_coor.isdigit():
            print("Wrong value sorry. Try again.. ")
            continue
        else:
            if index > 0:
                throw_pellets(int(x_coor)-1, int(y_coor)-1)
                print_grid(grid)
            else:
                index -= 1


main()
