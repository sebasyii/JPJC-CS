class ListNode:
    def __init__(self, DataValue="", PointerValue=0):
        self.__DataValue = DataValue  # String
        self.__PointerValue = PointerValue  # Integer

    def GetDataValue(self):
        return self.__DataValue

    def GetPointerValue(self):
        return self.__PointerValue

    def SetDataValue(self, newData):
        self.__DataValue = newData

    def SetPointerValue(self, newPointer):
        self.__PointerValue = newPointer


class Linkedlist:
    def __init__(self, limit):
        self.__Node = [None] + [ListNode() for i in range(limit)]
        for index in range(1, limit):
            self.__Node[index].SetPointerValue(index+1)
        self.__Start = 0  # Initial is 0
        self.__NextFree = 1

    def IsEmpty(self):
        return self.__Start == 0

    def DisplayLinkedList(self):
        print("START =", self.__Start)
        print("NEXTFREE =", self.__NextFree)

        # Header
        print("{0:^10}|{1:^20}|{2:^10}".format("index", "Data", "Pointer"))
        print("-"*42)
        for i in range(1, len(self.__Node)):
            print(
                f"{i:^10} | {self.__Node[i].GetDataValue():^20} | {self.__Node[i].GetPointerValue():^10}")

    def AddNode(self):
        NewItem = input("Enter item to add: ")
        self.__Node[self.__NextFree].SetDataValue(NewItem)
        if self.__Start == 0:
            self.__Start = self.__NextFree
            Temp = self.__Node[self.__NextFree].GetPointerValue()
            self.__Node[self.__NextFree].SetPointerValue(0)
            self.__NextFree = Temp

        else:
            # Traverse the list - starting at Start to find
            # The position at which to insert the new item
            Temp = self.__Node[self.__NextFree].GetPointerValue()

            if NewItem < self.__Node[self.__Start].GetDataValue():
                self.__Node[self.__NextFree].SetPointerValue(self.__Start)
                self.__Start = self.__NextFree
                self.__NextFree = Temp
            else:
                previous = 0
                current = self.__Start
                found = False

                while not found and current != 0:
                    if NewItem <= self.__Node[current].GetDataValue():
                        self.__Node[previous].SetPointerValue(self.__NextFree)
                        self.__Node[self.__NextFree].SetPointerValue(current)
                        self.__NextFree = Temp
                        found = True
                    else:
                        previous = current
                        current = self.__Node[current].GetPointerValue()

                if current == 0:
                    self.__Node[previous].SetPointerValue(self.__NextFree)
                    self.__Node[self.__NextFree].SetPointerValue(0)
                    self.__NextFree = Temp

    def IsFull(self):
        return self.__NextFree == -1

    def TraversalInOrder(self, Index):
        if Index != 0:
            print(self.__Node[Index].GetDataValue())
            self.TraversalInOrder(self.__Node[Index].GetPointerValue())

    def Traversal(self):
        self.TraversalInOrder(self.__Start)

    def TraversalInReverseOrder(self, Index):
        if Index != 0:
            self.TraversalInReverseOrder(self.__Node[Index].GetPointerValue())
            print(self.__Node[Index].GetDataValue())

    def ReverseTraversal(self):
        self.TraversalInReverseOrder(self.__Start)

    def RemoveNode(self):
        Item = input("Enter item to remove: ")
        previous = None
        current = self.__Start

        while (self.__Node[current].GetDataValue() != Item) and (self.__Node[current].GetPointerValue() != 0):
            previous = current
            current = self.__Node[current].GetPointerValue()
        if (self.__Node[current].GetDataValue() == Item):
            if previous == None:
                temp = self.__Start
                self.__Start = self.__Node[current].GetPointerValue()

            else:
                temp = current
                self.__Node[previous].SetPointerValue(
                    self.__Node[current].GetPointerValue())
            self.__Node[temp].SetPointerValue(self.__NextFree)
            self.__NextFree = temp
            self.__Node[temp].SetDataValue("REMOVED")
        else:
            print("ITEM NOT FOUND")


def main():
    fruitsList = Linkedlist(30)
    while True:
        print('1. Add an item')
        print('2. Traverse the linked list of used nodes and output the data values')
        print('3. Output all pointers and data values')
        print('4. Reverse traversal and display data values')
        print('5. Remove an item')
        print('X. Exit')

        option = input('Enter option: ')

        if option == '1':
            if fruitsList.IsFull():
                print("It is full")
                continue
            else:
                fruitsList.AddNode()
        elif option == '2':
            fruitsList.Traversal()
        elif option == '3':
            fruitsList.DisplayLinkedList()
        elif option == '4':
            fruitsList.ReverseTraversal()
        elif option == '5':
            if fruitsList.IsEmpty():
                print("No data in linked list. Nothing to remove.")
                continue
            fruitsList.RemoveNode()
        elif option == 'X':
            break
        else:
            print('*** INVALID OPTION *** \nTry again')


main()
