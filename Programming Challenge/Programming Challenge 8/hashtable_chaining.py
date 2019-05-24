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

    def addnode(self, id, title):
        newNode = BookRec(id, title)
        if self.isEmpty():
            self.__Start = None

        else:
            temp = self.__Start
            self.start = newNode
            newNode.setPointer(temp)

    def delnode(self, id):
        if self.__Start is not None:
            prev = None
            current = self.__Start
            while current.getBookID() != id and current.getPointer() is not None:
                prev = current
                current = current.getPointer()
            if prev is None:
                if self.__Start.getBookID() == id:
                    self.__Start = current.getPointer()
            elif current.getBookID() == id:
                prev.setPointer(current.getPointer())
