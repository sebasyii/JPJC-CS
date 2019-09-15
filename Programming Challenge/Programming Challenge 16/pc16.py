class ConnectionNode:
    def __init__(self, DataValue="", LeftChild=0, RightChild=0):
        self.__DataValue = str(DataValue)
        self.__LeftChild = int(LeftChild)
        self.__RightChild = int(RightChild)

    def getDataValue(self):
        return self.__DataValue

    def getLeftChild(self):
        return self.__LeftChild

    def getRightChild(self):
        return self.__RightChild

    def setDataValue(self, NewDataValue):
        self.__DataValue = str(NewDataValue)

    def setLeftChild(self, NewLeftChild):
        self.__LeftChild = int(NewLeftChild)

    def setRightChild(self, NewRightChild):
        self.__RightChild = int(NewRightChild)


class Robot:
    def __init__(self):
        self.__RobotData = [None] + [ConnectionNode() for i in range(25)]
        for i in range(1, 25):
            self.__RobotData[i].setLeftChild(i + 1)
        self.__Root = 1
        self.__NextFreeChild = 1

    def display(self):
        print(f"Root is {self.__Root}")
        print(f"NextFreeChild is {self.__NextFreeChild}")
        print(f'{"Data":^10} | {"LeftChild":^10} | {"RightChild":^10}')
        for data in range(1, len(self.__RobotData)):
            print(
                f"{self.__RobotData[data].getDataValue():^10} | {self.__RobotData[data].getLeftChild():^10} | {self.__RobotData[data].getRightChild():^10}"
            )

    def FindNode(self, NodeValue):
        Found = False
        CurrentPosition = self.__Root
        while (CurrentPosition <= 25) and (Found == False):
            if self.__RobotData[CurrentPosition].getDataValue() == NodeValue:
                Found = True
            else:
                CurrentPosition += 1
        if CurrentPosition > 25:
            return 0
        else:
            return CurrentPosition

    def AddToRobotData(self, NewDataItem, ParentItem, ThisMove):
        if self.__Root == 1 and self.__NextFreeChild == 1:
            self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].getLeftChild()
            self.__RobotData[self.__Root].setLeftChild(0)
            self.__RobotData[self.__Root].setDataValue(NewDataItem)
        else:
            # Check for parent
            ParentPosition = self.FindNode(ParentItem)
            if ParentPosition > 0:
                ExistingChild = self.FindNode(NewDataItem)
                if ExistingChild > 0:
                    ChildPointer = ExistingChild
                else:
                    ChildPointer = self.__NextFreeChild
                    self.__NextFreeChild = self.__RobotData[
                        self.__NextFreeChild
                    ].getLeftChild()
                    self.__RobotData[ChildPointer].setLeftChild(0)
                    self.__RobotData[ChildPointer].setDataValue(NewDataItem)
                if ThisMove == "L":
                    self.__RobotData[ParentPosition].setLeftChild(ChildPointer)
                else:
                    self.__RobotData[ParentPosition].setRightChild(ChildPointer)

    def PreOrderTraversal(self, index):
        if self.__Root == 1:
            return "Empty!"
        if index != 0:
            print(self.__RobotData[index].getDataValue())
            self.PreOrderTraversal(self.__RobotData[index].getLeftChild())
            self.PreOrderTraversal(self.__RobotData[index].getRightChild())


def main():
    robot = Robot()
    infile = open("SEARCHTREE.txt", "r")
    for line in infile:
        data, parent, move = line[:-1].split(",")
        robot.AddToRobotData(data, parent, move)
    infile.close()
    robot.display()
    robot.PreOrderTraversal(1)


main()
