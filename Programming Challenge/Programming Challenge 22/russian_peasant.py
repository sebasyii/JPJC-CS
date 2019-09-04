# Task 1

terms = []
total = 0
num1, num2 = input("Please enter 2 numbers(with space in between): ").split()
num1 = int(num1)
num2 = int(num2)


def russian_peasant_algo(num1, num2):
    global total
    if num2 == 0:
        return
    if num2 % 2 == 1:
        total += num1
    russian_peasant_algo(num1*2, int(num2//2))


russian_peasant_algo(num1, num2)
print(total)


# Task 2======================

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


Stack1 = Stack()

decNum = int(input("Enter a decimal Number: "))


def dec2bin(decNum):
    arr_bin = []
    while decNum != 0:
        newNum = decNum % 2
        decNum = decNum // 2
        Stack1.push(newNum)

    while Stack1.size() != 0:
        arr_bin.append(str(Stack1.pop()))

    return ''.join(arr_bin)


# Task 3
totalInBin = 0


def actual_russian_peasant_algorithm(binNum1, binNum2):
    global totalInBin
    if binNum2 == '0000':
        return
    if binNum2[-1] == '1':
        totalInBin = bin(int(binNum1, 2)+int(str(totalInBin), 2))
    binNum2 = '0' + binNum2
    actual_russian_peasant_algorithm(binNum1+'0', binNum2[:-1])


decNum1, decNum2 = input(
    "Please enter 2 numbers(with space in between): ").split()
decNum1 = int(decNum1)
decNum2 = int(decNum2)
actual_russian_peasant_algorithm(dec2bin(decNum1), dec2bin(decNum2))
print(totalInBin[2:])
