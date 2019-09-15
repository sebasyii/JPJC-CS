class Stack:
    def __init__(self):
        self.__items = []
        self.__top = 0

    def Push(self, item):
        self.__items.append(item)
        self.__top += 1

    def Pop(self):
        if self.isEmpty():
            return "stack is empty.nothing to pop"
        self.__top -= 1
        return self.__items.pop()

    def Peep(self):  # inspect the topmost item of the stack
        if self.isEmpty():
            return "stack is empty"
        return self.__items[self.__top - 1]

    def isEmpty(self):
        return self.__top == 0


def CheckNested(construct):  # construct is string
    leftBrackets = ["(", "[", "{"]
    rightBrackets = [")", "]", "}"]
    opStack = Stack()  # create a stack
    for i in range(len(construct)):
        if construct[i] in "({[":
            opStack.Push(construct[i])
        elif construct[i] in ")]}":
            if not opStack.isEmpty():
                topItem = opStack.Pop()
                if leftBrackets.index(topItem) != rightBrackets.index(construct[i]):
                    return False
                else:
                    return False
            else:  # nth on stack
                return False

    if not opStack.isEmpty():
        return False

    else:
        return True


def task3():
    infile = open("DATA.txt", "r")
    outfile = open("ERRORS.txt", "w")
    for line in infile:
        if CheckNested(line[:-1]) is False:
            print(line[:-1], file=outfile)
    outfile.close()
    infile.close()


task3()
