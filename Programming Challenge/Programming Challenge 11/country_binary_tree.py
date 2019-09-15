class Node:
    def __init__(self, data):
        self.__Data = data
        self.__LeftP = 0
        self.__RightP = 0

    def getData(self):
        return self.__Data

    def getLeftP(self):
        return self.__LeftP

    def getRightP(self):
        return self.__RightP

    def setLeftP(self, ptr):
        self.__LeftP = ptr

    def setRightP(self, ptr):
        self.__RightP = ptr

    def setData(self, data):
        self.__Data = data


class BinaryTree:
    def __init__(self, limit=5):
        self.__limit = limit
        self.__ThisTree = [None] + [Node("") for node in range(limit)]
        # Set Pointers
        for ptr in range(1, self.__limit):
            self.__ThisTree[ptr].setLeftP(ptr + 1)
        self.__ThisTree[self.__limit] = Node("")
        self.__Root = 0
        self.__NextFreePosition = 1

    def IsFull(self):
        return self.__NextFreePosition == 0

    def AddItemToBinaryTree(self, NewTreeItem):
        if self.IsFull():
            print("Binary Tree is full!")
            return

        if self.__Root == 0:
            self.__Root = self.__NextFreePosition

        else:
            CurrentPosition = self.__Root
            LastMove = "X"
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewTreeItem < self.__ThisTree[CurrentPosition].getData():
                    LastMove = "L"
                    CurrentPosition = self.__ThisTree[CurrentPosition].getLeftP()
                else:
                    LastMove = "R"
                    CurrentPosition = self.__ThisTree[CurrentPosition].getRightP()

            if LastMove == "R":
                self.__ThisTree[PreviousPosition].setRightP(self.__NextFreePosition)
            else:
                self.__ThisTree[PreviousPosition].setLeftP(self.__NextFreePosition)

        NewNextFreePosition = self.__ThisTree[
            self.__NextFreePosition
        ].getLeftP()  # set to next point
        self.__ThisTree[self.__NextFreePosition].setLeftP(0)
        self.__ThisTree[self.__NextFreePosition].setData(NewTreeItem)
        self.__NextFreePosition = NewNextFreePosition

    def OutputData(self):
        output = "ROOT = {}\n".format(self.__Root)
        output = output + "Nextfree={}\n".format(self.__NextFreePosition)
        output = output + "{:^5}{:^10}{:^5}{:^5}\n".format(
            "Index", "Data", "LeftPtr", "RightPtr"
        )
        for i in range(1, self.__limit):
            output = output + "{:^5}{:^10}{:^5}{:^5}\n".format(
                i,
                self.__ThisTree[i].getData(),
                self.__ThisTree[i].getLeftP(),
                self.__ThisTree[i].getRightP(),
            )
        return output

    def InOrderTraversal(self, index):
        if self.__Root == 0:
            return "Binary Tree is empty!"

        if index != 0:
            self.InOrderTraversal(self.__ThisTree[index].getLeftP())
            print(self.__ThisTree[index].getData())
            self.InOrderTraversal(self.__ThisTree[index].getRightP())


def main():
    tree = BinaryTree()
    NewItem = input("Enter a new item:")
    while NewItem != "XXX":
        tree.AddItemToBinaryTree(NewItem)
        NewItem = input("Enter a new item: ")
    print(tree.OutputData())
    tree.InOrderTraversal(3)


main()
