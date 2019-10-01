def main():
    times = 10
    list_of_walkers = []
    while times > 0:
        name_user_input = input("Enter the name: ")
        steps_taken = int(input(f"Please input {name_user_input} steps: "))
        list_of_walkers.append([name_user_input, steps_taken])
        times -= 1
        print("\n\n")
        more_input = input("Do you want to input more names? (Y/N): ")
        if more_input == "Y":
            continue
        else:
            break

    most_steps_member = list_of_walkers[0]
    for walker in list_of_walkers:
        if walker[1] > most_steps_member[1]:
            most_steps_member = walker

    infile = open("STAR.txt", "r")
    star, star_steps = infile.readline()[:-1].split(",")
    infile.close()
    print(f"Last week, {star} was 'Star of the Week' with {star_steps} steps taken")
    print(
        f"This week, {most_steps_member[0]} is 'Star of the Week' with {most_steps_member[1]} steps taken"
    )

    if int(star_steps) > most_steps_member[1]:
        print(
            f"\nThis week, {star} is still the 'Star of the Week' with {star_steps} steps taken"
        )
    else:
        outfile = open("STAR.txt", "w")
        outfile.write(f"{most_steps_member[0]},{most_steps_member[1]}")
        outfile.close()


main()
