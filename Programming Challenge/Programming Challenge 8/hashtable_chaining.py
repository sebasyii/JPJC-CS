class BookRec:
    def __init__(self, ID=None, title=None):
        self.__BookID = str(ID)
        self.__Title = str(title)
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


class Linkedlist:
    def __init__(self):
        self.__Start = None

    def __str__(self):
        output = ""
        temp = self.__Start
        i = 1
        while temp is not None:
            output += '{0}{1}{2}'.format(i, temp.getBookID(), temp.getTitle())
            temp = temp.getPointer()
            i += 1
        output += " None"
        return output

    def isEmpty(self):
        return self.__Start is None

    def AddNode(self, id, title):
        newNode = BookRec(id, title)
        if self.isEmpty():
            self.__Start = newNode

        else:
            temp = self.__Start
            self.start = newNode
            newNode.setPointer(temp)

    def DeleteNode(self,BookID):
        if not self.IsEmpty():         #Linkedlist is empty
            previous = None
            current = self.__start
            while current.getBookID() != BookID and current.getPointer() is not None:
                previous = current
                current = current.getPointer()
            if previous is None:               #firstnode to be removed
                self.__start = current.getPointer()
            elif current.getBookID() == BookID:
                previous.setPointer(current.getPointer())
            else: #data doesnt exist within the table
                print(BookID,"not found. Nothing to remove")
        else: #empty linked list
            print("No nodes in the the linked list. Nothing to remove.")

    def SearchNode(self,BookID):
        temp = self.__start
        while temp is not None:
            if temp.getBookID() == BookID:
                return True
            temp = temp.getPointer()
        return False
    
    def DisplayLinkedList(self):
        print("|{:^10}|{:^15}|{:^35}|{:^15}|".format("Index","BookID","Title","Pointer"))
        print("-"*80)
        for i in range(len(self.__ArrayOfNodes)):
            print("|{:^10}|{:^15}|{:^35}|{:^15}|".format(i,self._ArrayOfNodes[i].getBookID(),self.ArrayOfNodes[i].getTitle(),self._ArrayOfNodes[i].getPointer()))
        print("\n")
        print("Start = ",self.__start)
        print("NextFree = ",self.__nextfree)
    
class HashTable:
    def _init_(self,size):
        self.__Size = size
        self.__Slots = [LinkedList() for i in range(size)]

    def Hash(self,BookID):
        array = []
        total = 0
        for each in BookID:
            array.append(each)
        for i in range(len(array)):
            total = total + ord(array[i])
        ASCII = total%self.__size+1
        return ASCII

    def Display(self):
        print("  |{:^10}|{:^25}|".format("BookID","Title"))
        print(" ","_"*37)
        for i in range(self.__size):
            self.__Book[i].DisplayLinkedList()
            print(" ","_"*37)

    def Put(self,BookID,Title):
        ASCII = self.Hash(BookID)
        self.__Book[ASCII].AddNode(BookID,Title)

    def Remove(self,BookID):
        ASCII = self.Hash(BookID)
        self.__Book[ASCII].DeleteNode(BookID)

    def Search(self,BookID):
        ASCII = self.Hash(BookID)
        self.__Book[ASCII].SearchNode(BookID)
        

l = HashTable(17)
l.Put("CS733","Basic algorithms")
l.Put("AB944","Master Computing")
l.Put("KS293","Data structures")
l.Put("BK232","Programming exercises")
l.Put("PK199","Testing Python")
l.Display()
l.Remove("AB944")
l.Search("KS293")
l.Display()