class Node:
    def __init__(self, rootData):
        self.__rootData = rootData
        self.__leftChild = None
        self.__rightChild = None

    def getRootData(self):
        return self.__rootData

    def getLeftChild(self):
        return self.__leftData

    def getRightCchild(self):
        return self.__rightData

    def setRootData(self, rootData):
        self.__rootData = rootData

    def setLeftChild(self, ptr):
        self.__leftChild = ptr

    def setRightChild(self, ptr):
        self.__rightChild = ptr

class BinaryTree:
    def __init__(self):
        self.__start = None

    def getStart(self):
        return self.__start

    def insertBST(self, data):
        newNode = Node(data)
        previous = None
        current = getStart()
        if current == None:
            self.__start = newNode

        else:
            while current:
                if data < current.getRootData(): #Access left
                    previous = current
                    current = current.getLeftChild()
                else: #Access right
                    previous = current
                    current = current.getRightChild()
                    moveLeft = False

            if moveLeft == True:
                previous.setLeftChild(newNode)
            elif moveLeft == False:
                previous = setRightChild(newNode)
    def preOrder(self, current):
        if current:
            print(current.getRootData())
            self.preOrder(current.getLeftChild())
            self.preorder(curretnt.getRightChild())

    def inOrder(self, current):
        if current:
            self.inOrder(current.getLeftChild())
            print(current.getRootData())
            self.inOrder(current.getRightChild())

    def postOrder(self, current):
        if current:
            self.inOrder(current.getLeftChild())
            self.inOrder(current.getRightChild())
            print(current.getRootData())


def main():
    fruits = ["mango","orange","banana","durian","pineapple", "apple","grapes"]
    bt = BinaryTree()
    for each in fruits:
        bt.insertBST(each)
    bt.preOrder(bt.getStart())
    print()
    bt.inOrder(bt.getStart())
    print()
    bt.postOrder(bt.getStart())
                '
