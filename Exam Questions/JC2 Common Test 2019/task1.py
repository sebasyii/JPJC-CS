file = open("marks.txt", "r")
details = []
for line in file:
    details.append(line.strip().split(","))
file.close()

total = int(0)
for i in range(len(details)):
    for j in range(1, 5):
        total = total + float(details[i][j])
    details[i].append(round(total, 1))
    total = int(0)

for i in range(len(details)):
    for j in range(len(details)):
        if details[i][5] > details[j][5]:
            details[i], details[j] = details[j], details[i]

print("{0:7}{1:30}{2:10}".format("No.", "Name of student", "Total exam marks"))
for i in range(len(details)):
    print("{0:<7}{1:<30}{2:<10}".format(i + 1, details[i][0], details[i][5]))

minimum_mark = input("What is the minimum mark? ")
while not minimum_mark.isdigit():
    print("INVALID Mark!\n")
    minimum_mark = input("What is the minimum mark? ")
lessThanXList = []
for i in range(len(details)):
    if details[i][5] < float(minimum_mark):
        lessThanXList.append(details[i])
for i in range(len(lessThanXList)):
    print(lessThanXList[i][0], lessThanXList[i][5])
    print(len(lessThanXList), "Students obtained less than", minimum_mark, "marks.")
