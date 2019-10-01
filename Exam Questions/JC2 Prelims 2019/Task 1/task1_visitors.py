file = open("VISITORS.txt", "r")  # open and close input file, correct mode
file.readline()  # discard/skip first line of data
touristNumbers = list()
for line in file:  # read every record into touristNumbers
    year, month, number = line[:-1].split(",")
    touristNumbers.append((year, month, number))
file.close()

touristByYear = dict()  # organise records into dict (key:value is year:touristNumbers)
for i in range(len(touristNumbers)):
    if touristNumbers[i][0] in touristByYear:  # method to total up visitors (by year)
        touristByYear[touristNumbers[i][0]] = int(
            touristByYear[touristNumbers[i][0]]
        ) + int(touristNumbers[i][2])
    else:
        touristByYear[touristNumbers[i][0]] = int(touristNumbers[i][2])

startYear = input("Start year : ")  # user input for start & end years
endYear = input("End year : ")
while (
    int(startYear) < 1978 or int(endYear) > 2018 or int(startYear) > int(endYear)
):  # validation
    print(
        "Years must be between 1978 to 2018 inclusive.\nStart year must be earlier than end year.\n"
    )  # error messages
    startYear = input("Start year : ")
    endYear = input("End year : ")

print("{:<10}{:<10}".format("Year", "Visitors"))  # proper heading and format
key = startYear
endKey = int(endYear)
while int(key) < endKey + 1:  # display records
    print("{:<10}{:<10}".format(str(key), touristByYear[str(key)]))
    key = int(key) + 1

# Test case 1: start year > end year, start year = 2000, end year = 1999, error message and get user input again
# Test case 2: start year before 1978/ end year after 2018, error message and get user input again
# Test case 3: Valid start year and end year, successfully display years and total visitors
# Test case 4: Boundary data: start year is 1978/ end year is 2018, display years and total visitors successfully
