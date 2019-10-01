class Node:
    def __init__(self, Data="", Priority=-1, Pointer=-1):
        self.__Data = str(Data)
        self.__Priority = int(Priority)
        self.__Pointer = int(Pointer)

    def getData(self):
        return self.__Data

    def getPriority(self):
        return self.__Priority

    def getPointer(self):
        return self.__Pointer

    def setData(self, Data):
        self.__Data = Data

    def setPriority(self, Priority):
        self.__Priority = Priority

    def setPointer(self, Pointer):
        self.__Pointer = Pointer


class PQueue:
    def __init__(self):  # Initialise Method
        self.__ThisPQueue = [Node() for i in range(10)]
        self.__Front = -1
        self.__Rear = -1
        self.__NextFree = int(0)
        for i in range(len(self.__ThisPQueue) - 1):
            self.__ThisPQueue[i].setPointer(i + 1)

    def IsEmpty(self):
        return self.__Front == -1 and self.__Rear == -1

    def IsFull(self):
        return self.__NextFree == -1

    def JoinPQueue(self, NewItem, Priority):
        if self.IsFull():
            print("Queue full.")
            return
        # Else Do this
        else:
            self.__ThisPQueue[self.__NextFree].setData(NewItem)
            self.__ThisPQueue[self.__NextFree].setPriority(Priority)
            # Pointing to new node
            newNode = self.__NextFree
            self.__NextFree = self.__ThisPQueue[self.__NextFree].getPointer()
            # Set new pointer to -1
            self.__ThisPQueue[newNode].setPointer(-1)

            # If empty
            if self.IsEmpty():
                self.__Front = newNode
                self.__Rear = newNode

            # Lesser than The last item priority
            elif Priority <= self.__ThisPQueue[self.__Rear].getPriority():
                self.__ThisPQueue[self.__Rear].setPointer(newNode)
                self.__Rear = newNode

            elif Priority > self.__ThisPQueue[self.__Front].getPriority():
                self.__ThisPQueue[newNode].setPointer(self.__Front)
                self.__Front = newNode

            # In between
            else:
                previous = -1
                current = self.__Front
                while (
                    self.__ThisPQueue[current].getPriority() >= Priority
                    and current != -1
                ):
                    previous = current
                    current = self.__ThisPQueue[current].getPointer()

                self.__ThisPQueue[previous].setPointer(newNode)
                self.__ThisPQueue[newNode].setPointer(current)

                if self.__ThisPQueue[self.__Rear].getPointer() != -1:
                    self.__Rear = self.__ThisPQueue[self.__Rear].getPointer()
            print(f"{NewItem} is added with {str(Priority)} Priority")

    def LeavePQueue(self):
        if self.IsEmpty():
            print("Queue Empty")
            return

        data = self.__ThisPQueue[self.__Front].getData()
        self.__ThisPQueue[self.__Front].setData("")
        self.__ThisPQueue[self.__Front].setPriority(-1)

        temp = self.__NextFree

        self.__NextFree = self.__Front
        self.__Front = self.__ThisPQueue[self.__Front].getPointer()
        self.__ThisPQueue[self.__NextFree].setPointer(temp)

        if self.__Front == -1:
            self.__Rear = -1
        return data

    def OutputPQueue(self):
        print(f"Front Pointer: {self.__Front}")
        print(f"Rear Pointer: {self.__Rear}")
        print(f"NextFree: {self.__NextFree}")
        print()
        print(f'{"Index":^10} {"Data":^20} {"Pointer":^10} {"Priority":^10}')
        for idx in range(len(self.__ThisPQueue)):
            print(
                f"{idx:^10} {self.__ThisPQueue[idx].getData():^20} {self.__ThisPQueue[idx].getPointer():^10} {self.__ThisPQueue[idx].getPriority():^10}"
            )


def menu():
    print("\n")
    print("Patient Queue Menu\n")
    print("1) Add patient to PQueue")
    print("2) Remove patient from PQueue")
    print("3) Display PQueue")
    print("4) Exit Program")


def main():
    JPQueue = PQueue()
    infile = open("PATIENTS.txt", "r")
    for line in infile:
        if line[-1] == "\n":
            name, priority = line[:-1].split(",")
            JPQueue.JoinPQueue(name, int(priority))
        else:
            name, priority = line.split(",")
            JPQueue.JoinPQueue(name, int(priority))
    infile.close()
    while True:
        menu()
        option = input("Enter your choice:")
        if option == "1":
            name = input("Who do you want to add: ")
            priority = int(input(f"What is {name} priority: "))
            JPQueue.JoinPQueue(name, priority)
        elif option == "2":
            print(f"\n{JPQueue.LeavePQueue()} is removed\n")
        elif option == "3":
            JPQueue.OutputPQueue()
        else:
            break

    JPQueue.OutputPQueue()


main()
