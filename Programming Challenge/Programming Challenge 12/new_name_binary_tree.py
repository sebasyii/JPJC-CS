class Node:
    def __init__(self, data="", leftPtr=-1, rightPtr=-1):
        self.__data = str(data)
        self.__leftPtr = int(leftPtr)
        self.__rightPtr = int(rightPtr)

    def getData(self):
        return self.__data

    def getLeftPtr(self):
        return self.__leftPtr

    def getRightPtr(self):
        return self.__rightPtr

    def setData(self, data):
        self.__data = data

    def setLeftPtr(self, leftPtr):
        self.__leftPtr = leftPtr

    def setRightPtr(self, rightPtr):
        self.__rightPtr = rightPtr


class Tree:
    def __init__(self, size=10):
        self.__tree = [Node() for i in range(size)]
        self.__root = int(-1)
        self.__nextfree = int(0)
        for i in range(size - 1):
            self.__tree[i].setLeftPtr(i + 1)

    def getRoot(self):
        return self.__root

    def add(self, newItem):
        if self.__nextfree == -1:
            print("No free node!")
            return

        temp = self.__tree[self.__nextfree].getLeftPtr()
        self.__tree[self.__nextfree].setData(str(newItem))
        self.__tree[self.__nextfree].setLeftPtr(-1)
        self.__tree[self.__nextfree].setRightPtr(-1)
        # If it is empty
        if self.__root == -1:
            self.__root = self.__nextfree
        else:
            current = self.__root
            LastMove = "X"
            while current != -1:
                previous = current
                if newItem < self.__tree[current].getData():
                    current = self.__tree[current].getLeftPtr()
                    LastMove = "L"
                else:
                    current = self.__tree[current].getRightPtr()
                    LastMove = "R"
            if LastMove == "L":
                self.__tree[previous].setLeftPtr(self.__nextfree)
            else:
                self.__tree[previous].setRightPtr(self.__nextfree)
        self.__nextfree = temp

    def __str__(self):
        output = "ROOT = {}\n".format(self.__root)
        output = output + "Nextfree={}\n".format(self.__nextfree)
        output = output + "{:^5}{:^10}{:^5}{:^5}\n".format(
            "Index", "Data", "LeftP", "RightP"
        )
        for i in range(10):
            output = output + "{:^5}{:^10}{:^5}{:^5}\n".format(
                i,
                self.__tree[i].getData(),
                self.__tree[i].getLeftPtr(),
                self.__tree[i].getRightPtr(),
            )
        return output


def main():
    tree = Tree(10)
    tree.add("Dave")
    tree.add("Fred")
    tree.add("Ed")
    tree.add("Greg")
    tree.add("Bob")
    tree.add("Cid")
    tree.add("Ali")
    print(tree)


main()
