infile = open("RAINFALL.txt", "r")

header = infile.readline()[:-1]


list_of_dates = []

for line in infile:
    year_month, no_of_rainy_days = line[:-1].split(",")
    year, month = year_month.split("-")
    list_of_dates.append([year, month, no_of_rainy_days])

infile.close()

rainfall_years = []

while True:
    total_rainfall = 0
    for idx in range(len(list_of_dates) - 1):
        curr = list_of_dates[idx]
        nxt = list_of_dates[idx + 1]

        if curr[0] == nxt[0]:
            total_rainfall += int(curr[2])
            continue
        else:
            total_rainfall += int(curr[2])
            rainfall_years.append([curr[0], total_rainfall])
            total_rainfall = 0

    break

# Write to file

outfile = open("RAINFALLYEAR.txt", "w")
outfile.write("Year,Rainy Days\n")
for year in rainfall_years:
    outfile.write(f"{year[0]},{year[1]}\n")

outfile.close()


# ------------ Task 1.2 --------------------


def ShowMenu():
    print("1. Query total rainy days in any year")
    print("2. Query by year the month of highest rainy days")
    print("3. -1 to Exit")


def Query1(year):
    for data in rainfall_years:
        if year == data[0]:
            print(data[1])


def Query2(year):
    list_of_months = [
        "January",
        "Feburary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    list_of_data = []
    for data in list_of_dates:
        if data[0] == year:
            list_of_data.append(data)
    largest = list_of_data[0][2]

    for j in list_of_data:
        if int(j[2]) > int(largest):
            largest = j[2]

    for no_of_rain in list_of_data:
        if largest == no_of_rain[2]:
            if no_of_rain[1][0] == "0":
                return list_of_months[int(no_of_rain[1][1]) - 1]
            return list_of_months[int(no_of_rain[1]) - 1]


def main():
    loop = True

    while loop:
        ShowMenu()
        print()
        user_input = input("Choose a choice: ")
        while int(user_input) > 3 or int(user_input) == 0 or int(user_input) < -1:
            print("\nPlease enter a valid choice: ")
            user_input = input("Choose a valid choie: ")
        if user_input == "1":
            user_year = input("Please enter a valid year between 1982 and 2018: ")
            while (
                int(user_year) < 1982
                or int(user_year) > 2018
                or not user_input.isdigit()
            ):
                print("\nPlease enter a valid year")
                user_year = input("Please enter a valid year between 1982 and 2018: ")

            print()
            Query1(user_year)
            continue

        elif user_input == "2":
            user_year = input("Please enter a valid year between 1982 and 2018: ")
            while (
                int(user_year) < 1982
                or int(user_year) > 2018
                or not user_input.isdigit()
            ):
                print("\nPlease enter a valid year")
                user_year = input("Please enter a valid year between 1982 and 2018: ")

            print()
            print(Query2(user_year))
            continue

        else:
            loop = False
            break


main()
