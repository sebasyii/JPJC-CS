class BookRec:
    def __init__(self, BookID="", Title=""):
        self.__BookID = str(BookID)
        self.__Title = str(Title)
        self.__Pointer = None

    def getBookID(self):
        return self.__BookID

    def getTitle(self):
        return self.__Title

    def getPointer(self):
        return self.__Pointer

    def setBookID(self, BookID):
        self.__BookID = BookID

    def setTitle(self, Title):
        self.__Title = Title

    def setPointer(self, Pointer):
        self.__Pointer = Pointer


class LinkedList:
    def __init__(self):
        self.__Start = None

    def getStart(self):
        return self.__Start

    def IsEmpty(self):
        return self.__Start == None

    def __str__(self):
        output = ""
        temp = self.__Start
        while temp is not None:
            output += f"{temp.getBookID():<10}{temp.getTitle():<30}"
            temp = temp.getPointer()

        return output

    def AddNode(self, BookID, Title):
        if self.IsEmpty():
            self.__Start = BookRec(BookID, Title)
        else:
            temp = self.__Start
            self.__Start = BookRec(BookID, Title)
            self.__Start.setPointer(temp)

    def DeleteNode(self, BookID):
        if self.IsEmpty():
            print("List Empty")
            return False
        else:
            prev = None
            curr = self.__Start
            while BookID != curr.getBookID() and curr is not None:
                prev = curr
                curr = curr.getPointer()
            # If first element
            if prev is None:
                if BookID == curr.getBookID():
                    self.__Start = curr.getPointer()
                else:
                    print("BookID is not found. Can't be deleted")
                    return False

            elif BookID == curr.getBookID():
                prev.setPointer(curr.getPointer())
                print("BookID deleted.")
                return True
            else:
                print("Cannot find. Can' delete.")
                return False

    def SearchNode(self, BookID):
        curr = self.__Start
        while curr is not None:
            if curr.getBookID() == BookID:
                return True
            curr = curr.getPointer()
        return False


class HashTable:
    def __init__(self, Size):
        self.__Size = Size
        self.__Slots = [LinkedList() for i in range(self.__Size)]

    def Hash(self, BookID):
        char_total = 0
        for char in BookID:
            char_total += ord(char)
        address = char_total % self.__Size + 1
        return address

    def Display(self):
        print(f'\n{"BookID":<10}{"Title":<30}')
        for Slot in self.__Slots:
            print(f"{Slot}")

    def Put(self, BookID, Rec):
        address = self.Hash(BookID)
        self.__Slots[address].AddNode(BookID, Rec)

    def Remove(self, BookID):
        address = self.Hash(BookID)
        if self.__Slots[address].SearchNode(BookID) == True:
            self.__Slots[address].DeleteNode(BookID)
        else:
            print("BookID is not found.")
            return False

    def Search(self, BookID):
        address = self.Hash(BookID)
        if self.__Slots[address].SearchNode(BookID) == False:
            print("BookID not found")
            return False
        else:
            print("Found")
            return True


def main():
    records = HashTable(17)
    records.Put("CS733", "Basic algorithms")
    records.Put("AB944", "Master Computing")
    records.Put("KS293", "Data structures")
    records.Put("BK232", "Programming exercises")
    records.Put("PK199", "Testing Python")
    records.Display()
    records.Remove("AB944")
    records.Display()
    records.Search("KS293")


main()
