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
    def __init__(self, limit=20):
        self.__ThisTree = [None] + [Node("") for node in range(limit)]
        # Set Pointers
        for ptr in range(1, limit):
            self.__ThisTree[ptr].setLeftP(ptr+1)
        self.__ThisTree[limit] = Node("")
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
            LastMove = 'X'
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewTreeItem < self.__ThisTree[CurrentPosition].getData():
                    LastMove = 'L'
                    CurrentPosition = self.__ThisTree[CurrentPosition].getLeftP(
                    )
                else:
                    LastMove = 'R'
                    CurrentPosition = self.__ThisTree[CurrentPosition].getRightP(
                    )

            if LastMove == 'R':
                self.__ThisTree[PreviousPosition].setRightP(
                    self.__NextFreePosition)
            else:
                self.__ThisTree[PreviousPosition].setLeftP(
                    self.__NextFreePosition)

        NewNextFreePosition = self.__ThisTree[self.__NextFreePosition].getLeftP(
        )
        self.__ThisTree[self.__NextFreePosition].setLeftP(0)
        self.__ThisTree[self.__NextFreePosition].setData(NewTreeItem)
        self.__NextFreePosition = NewNextFreePosition

    def OutputData(self):
        print('Root: ' + str(self.__Root))
        print('NextFreePosition: ' + str(self.__NextFreePosition))
        print('Tree:')
        for i in range(1, 21):
            CurNode = self.__ThisTree[i]
            print(str(i) + ': ' + str(CurNode.getData()))

    def InOrderTraversal(self, index):
        if self.__Root == 0:
            return 'Binary Tree is empty!'

        if index != 0:
            self.InOrderTraversal(self.__ThisTree[index].getLeftP())
            print(self.__ThisTree[index].getData())
            self.InOrderTraversal(self.__ThisTree[index].getRightP())


def main():
    tree = BinaryTree()
    list_of_countries = ['INDIA', 'NEPAL', 'MALAYSIA',
                         'SINGAPORE', 'BURMA', 'CANADA', 'LATVIA']
    #NewItem = input('Enter a new item:')
    '''
    while NewItem != 'XXX':
        tree.AddItemToBinaryTree(NewItem)
        NewItem = input('Enter a new item: ')
    '''
    for country in list_of_countries:
        tree.AddItemToBinaryTree(country)

    tree.OutputData()
    tree.InOrderTraversal(3)


main()
