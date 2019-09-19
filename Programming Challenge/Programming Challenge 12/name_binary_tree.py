class Node:
    def __init__(self, data):
        self.__data = data
        self.__leftChild = 0
        self.__rightChild = 0

    def get_data(self):
        return self.__data

    def get_left_child(self):
        return self.__leftChild

    def get_right_child(self):
        return self.__rightChild

    def set_data(self, data):
        self.__data = data

    def set_left_child(self, ptr):
        self.__leftChild = ptr

    def set_right_child(self, ptr):
        self.__rightChild = ptr


class Tree:
    def __init__(self, limit):
        self.__root = -1
        self.__limit = limit
        self.__nextFreePosition = 1
        self.__tree = [None] + [Node("") for i in range(self.__limit)]
        for i in range(1, self.__limit):
            self.__tree[i].set_left_child(i + 1)
        self.__tree[self.__limit].set_left_child(0)

    def add(self, newItem):
        if self.__nextFreePosition == 0:
            print("Binary Tree is full")
            return

        if self.__root == -1:
            self.__root = self.__nextFreePosition

        else:
            curr = self.__root
            LastMove = "X"
            while curr != 0:
                pre = curr
                if newItem < self.__tree[curr].get_data():
                    LastMove = "L"
                    curr = self.__tree[curr].get_left_child()
                else:
                    LastMove = "R"
                    curr = self.__tree[curr].get_right_child()

            if LastMove == "R":
                self.__tree[pre].set_right_child(self.__nextFreePosition)
            else:
                self.__tree[pre].set_left_child(self.__nextFreePosition)

        # Get the next pointer
        new_next_free = self.__tree[self.__nextFreePosition].get_left_child()
        self.__tree[self.__nextFreePosition].set_data(newItem)  # set the data
        self.__tree[self.__nextFreePosition].set_left_child(0)  # Set it to last node
        self.__nextFreePosition = new_next_free

    def __str__(self):  # print method to display tree on screen
        output = "ROOT = {}\n".format(self.__root)
        output = output + "Nextfree={}\n".format(self.__nextFreePosition)
        output = output + "{:^5}{:^10}{:^5}{:^5}\n".format(
            "Index", "Data", "LeftPtr", "RightPtr"
        )
        for i in range(1, self.__limit):
            output = output + "{:^5}{:^10}{:^5}{:^5}\n".format(
                i,
                self.__tree[i].get_data(),
                self.__tree[i].get_left_child(),
                self.__tree[i].get_right_child(),
            )
        return output

    def inOrderTraversal(self, index):
        #If its empty
        if self.__root == -1:
            return "Binary Tree is empty!"

        if index != 0:
            self.inOrderTraversal(self.__tree[index].get_left_child())
            print(self.__tree[index].get_data())
            self.inOrderTraversal(self.__tree[index].get_right_child())


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
    tree.inOrderTraversal(1)


main()
