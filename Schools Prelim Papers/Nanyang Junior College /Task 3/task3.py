class Node:
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None

    def getKey(self):
        return self.__key

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def setKey(self, key):
        self.__key = key

    def setLeft(self, left):
        self.__Left = left

    def setRight(self, right):
        self.__right = right

    def insert(self, key):
        if self.__key == key:
            return False
        elif key < self.__key:
            if self.__left:
                return self.__left.insert(key)
            else:
                self.__left = Node(key)
                return True
        else:
            if self.__right:
                return self.__right.insert(key)
            else:
                self.__right = Node(key)
                return True

    def inorder(self, l):
        if self.__left:
            self.__left.inorder(l)
        l.append(self.__key)
        if self.__right:
            self.__right.inorder(l)
        return l


class Tree:
    def __init__(self):
        self.__root = None

    def add(self, key):
        if self.__root:
            return self.__root.insert(key)
        elif self.__root is None:
            self.__root = Node(key)
            return True

    def printTreeInOrder(self):
        if self.__root:
            return self.__root.inorder([])
        else:
            return []


def CreateTreeFromArray(arr):
    tree = Tree()
    for num in arr:
        tree.add(num)

    print(tree.printTreeInOrder())


bst = [11, 6, 1, 14, 16, 7, 17, 20, 13, 9, 15, 8, 5, 4, 2]


def sort_arr(arr):
    for i in range(len(bst)):
        for j in range(len(bst) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)


print(bst)
sort_arr(bst)
# CreateTreeFromArray(bst)
