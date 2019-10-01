def menu():
    print("\n" + "-" * 76)
    print("1. Add an item" + " " * (76 - 15) + "|")
    print(
        "2. Traverse the linked list of used nodes and output the data values"
        + " " * 7
        + "|"
    )
    print("3. Output all pointers and data values" + " " * 37 + "|")
    print(
        "4. Traverse the linked list of used nodes and out the data values reversely"
        + "|"
    )
    print("X. Exit" + " " * 68 + "|")
    print("-" * 76 + "\n")


class ListNode:
    def __init__(self, DataValue="", PointerValue=0):
        self.__DataValue = str(DataValue)
        self.__PointerValue = int(PointerValue)

    def getDataValue(self):
        return self.__DataValue

    def getPointerValue(self):
        return self.__PointerValue

    def setDataValue(self, DataValue):
        self.__DataValue = DataValue

    def setPointerValue(self, PointerValue):
        self.__PointerValue = PointerValue


class LinkedList:
    def __init__(self):  # Initialise Method
        self.__Node = [None] + [ListNode() for i in range(30)]
        self.__Start = 0
        self.__NextFree = 1
        for i in range(1, len(self.__Node) - 1):
            self.__Node[i].setPointerValue(i + 1)

    def IsEmpty(self):
        return self.__Start == 0

    def IsFull(self):
        return self.__NextFree == 0

    def OutputLinkedList(self):
        print(f"NextFree: {self.__NextFree}")
        print(f"Start: {self.__Start}\n")
        print(f'{"Data Value":^15} {"Pointer Value":^10}')
        for i in range(1, len(self.__Node)):
            print(
                f"{self.__Node[i].getDataValue():^15} {self.__Node[i].getPointerValue():^10}"
            )

    def AddNode(self):
        NewItem = input("Enter your Data: ")
        self.__Node[self.__NextFree].setDataValue(NewItem)

        # Empty
        if self.__Start == 0:
            self.__Start = self.__NextFree
            Temp = self.__Node[self.__NextFree].getPointerValue()
            self.__Node[self.__NextFree].setPointerValue(0)
            self.__NextFree = Temp
        else:
            # Find Position to insert

            Temp = self.__Node[self.__NextFree].getPointerValue()

            if NewItem < self.__Node[self.__Start].getDataValue():

                self.__Node[self.__NextFree].setPointerValue(self.__Start)
                self.__Start = self.__NextFree
                self.__NextFree = Temp

            else:
                Previous = 0
                Current = self.__Start
                Found = False

                while not Found and Current != 0:
                    if NewItem <= self.__Node[Current].getDataValue():
                        self.__Node[Previous].setPointerValue(self.__NextFree)
                        self.__Node[self.__NextFree].setPointerValue(Current)
                        self.__NextFree = Temp
                        Found = True

                    else:
                        Previous = Current
                        Current = self.__Node[Current].getPointerValue()

                if Current == 0:
                    self.__Node[Previous].setPointerValue(self.__NextFree)
                    self.__Node[self.__NextFree].setPointerValue(Current)
                    self.__NextFree = Temp

    def Traversal(self):
        self.TraversalInOrder(self.__Start)

    def TraversalInOrder(self, Index):
        if Index != 0:
            print(self.__Node[Index].getDataValue())
            self.TraversalInOrder(self.__Node[Index].getPointerValue())

    def ReverseTraversal(self):
        self.TraversalInReverseOrder(self.__Start)

    def TraversalInReverseOrder(self, Index):
        if Index != 0:
            self.TraversalInOrder(self.__Node[Index].getPointerValue())
            print(self.__Node[Index].getDataValue())


def main():
    fruits_linked_list = LinkedList()
    loop = True
    while loop:
        menu()

        user_choice = input("Enter a choice: ")
        if user_choice == "1":
            print("\n")
            if not fruits_linked_list.IsFull():
                fruits_linked_list.AddNode()
            else:
                print("List is full. \n")
        elif user_choice == "2":
            print("\n")
            if not fruits_linked_list.IsEmpty():
                fruits_linked_list.Traversal()
            else:
                print("Linked List is empty.")
        elif user_choice == "3":
            print("\n")
            fruits_linked_list.OutputLinkedList()
        elif user_choice == "4":
            print("\n")
            if not fruits_linked_list.IsEmpty():
                fruits_linked_list.ReverseTraversal()
            else:
                print("Linked list is empty.")
        elif user_choice == "X":
            print("You chose eXit\n")
            loop = False
            break
        else:
            print("You typed an Invalid option. Type again.\n")
            continue


main()
