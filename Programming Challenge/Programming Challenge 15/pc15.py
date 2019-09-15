def CreateUpdateFile():
    results = open("RESULTS.txt", "r")
    first_match = results.readline()
    modified_data = first_match.split()
    new_file = open("NEWFILE.txt", "a")
    if int(modified_data[1]) > int(modified_data[3]):
        new_file.write(
            "{0},{1},{2},{3}\n".format(
                modified_data[0], "W", modified_data[1], modified_data[3]
            )
        )
        new_file.write(
            "{0},{1},{2},{3}\n".format(
                modified_data[2], "L", modified_data[3], modified_data[1]
            )
        )
    elif int(modified_data[3]) > int(modified_data[1]):
        new_file.write(
            "{0},{1},{2},{3}\n".format(
                modified_data[0], "L", modified_data[1], modified_data[3]
            )
        )
        new_file.write(
            "{0},{1},{2},{3}\n".format(
                modified_data[2], "W", modified_data[3], modified_data[1]
            )
        )
    results.close()
    new_file.close()


##CreateUpdateFile()


def newCreateUpdateFileTask2():
    results = open("RESULTS.txt", "r")
    new_file = open("NEWFILE.txt", "w")
    for data in results:
        modified_data = data.split()
        if int(modified_data[1]) > int(modified_data[3]):
            new_file.write(
                "{0},{1},{2},{3}\n".format(
                    modified_data[0], "W", modified_data[1], modified_data[3]
                )
            )
            new_file.write(
                "{0},{1},{2},{3}\n".format(
                    modified_data[2], "L", modified_data[3], modified_data[1]
                )
            )
        elif int(modified_data[3]) > int(modified_data[1]):
            new_file.write(
                "{0},{1},{2},{3}\n".format(
                    modified_data[0], "L", modified_data[1], modified_data[3]
                )
            )
            new_file.write(
                "{0},{1},{2},{3}\n".format(
                    modified_data[2], "W", modified_data[3], modified_data[1]
                )
            )
        else:
            new_file.write(
                "{0},{1},{2},{3}\n".format(
                    modified_data[0], "D", modified_data[1], modified_data[3]
                )
            )
            new_file.write(
                "{0},{1},{2},{3}\n".format(
                    modified_data[2], "D", modified_data[3], modified_data[1]
                )
            )

    results.close()
    new_file.close()


newCreateUpdateFileTask2()


def ComputeTeamStat(team_name):
    new_file = open("NEWFILE.txt", "r")
    games_played = 0
    games_won = 0
    games_drawn = 0
    games_lost = 0
    goals_for = 0
    goals_lost = 0

    points = 0

    for data in new_file:
        split_data = data[:-1].split(",")
        if split_data[0] == team_name:
            games_played += 1
            if split_data[1] == "W":
                games_won += 1
                points += 3
            elif split_data[1] == "L":
                games_lost += 1
            else:
                games_drawn += 1
                points += 1
            goals_for += int(split_data[2])
            goals_lost += int(split_data[3])

    goal_diff = goals_for - goals_lost
    print(
        "{0:<10} {1:<3} {2:<3} {3:<3} {4:<3} {5:<3} {6:<3} {7:<3} {8:<3}".format(
            team_name,
            games_played,
            games_won,
            games_drawn,
            games_lost,
            goals_for,
            goals_lost,
            goal_diff,
            points,
        )
    )
    return [team_name, points, goal_diff]


print(
    "{0:<10} {1:<3} {2:<3} {3:<3} {4:<3} {5:<3} {6:<3} {7:<3} {8:<3}".format(
        "Team", "P", "W", "D", "L", "GF", "GA", "GD", "Points"
    )
)


def GenerateTable():
    infile = open("TEAMS.txt", "r")
    arr_data = []
    for team_name in infile:
        arr_data.append(ComputeTeamStat(team_name[:-1]))

    for i in range(0, len(arr_data) - 1):
        for j in range(0, len(arr_data) - i - 1):
            if int(arr_data[j][1]) < int(arr_data[j + 1][1]):
                arr_data[j], arr_data[j + 1] = arr_data[j + 1], arr_data[j]
            elif int(arr_data[j][1]) == int(arr_data[j + 1][1]):
                if int(arr_data[j][2]) < int(arr_data[j + 1][2]):
                    arr_data[j], arr_data[j + 1] = arr_data[j + 1], arr_data[j]

    print()
    print()
    print("----------- Organize Data ----------")
    for data in arr_data:
        ComputeTeamStat(data[0])

    infile.close()


GenerateTable()
