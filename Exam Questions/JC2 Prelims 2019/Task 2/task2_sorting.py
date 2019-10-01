def SomeSort(SomeList):
    count = 0  ##for counting number of comparisons
    for Pointer in range(1, len(SomeList)):  # start from 2nd element in list
        ItemToBeInserted = SomeList[Pointer]
        CurrentItem = Pointer - 1
        count = count + 1  # compare numbers, increment count
        while (SomeList[CurrentItem] > ItemToBeInserted) and (CurrentItem >= 0):
            SomeList[CurrentItem + 1] = SomeList[CurrentItem]
            SomeList[CurrentItem] = ItemToBeInserted
            CurrentItem = CurrentItem - 1
            count = count + 1  # compare numbers, increment count
        SomeList[CurrentItem + 1] = ItemToBeInserted
    print("Number of comparisons:", count)
    return SomeList


def BubbleSort(NumberList):
    count = 0  ##for counting number of comparisons
    for i in range(len(NumberList) - 1):
        for j in range(len(NumberList) - 1):
            count = count + 1  # compare numbers, increment count
            if NumberList[j] > NumberList[j + 1]:
                temp = NumberList[j]
                NumberList[j] = NumberList[j + 1]
                NumberList[j + 1] = temp
    print("Number of comparisons:", count)
    return NumberList


print(SomeSort([435, 646, 344, 54, 23, 98, 789, 212, 847, 201, 733]))
print(BubbleSort([435, 646, 344, 54, 23, 98, 789, 212, 847, 201, 733]))
