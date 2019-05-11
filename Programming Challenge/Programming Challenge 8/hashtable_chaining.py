class BookRec():
    def __init__(self, ID=None, title=None):
        self.__BookID = str(ID)
        self.__Title = str(title)
        self.__pointer = None


class Linkedlist:
    def __init__(self):
        self.__start = None

    def __str__(self):
        output = ""
        temp = self.__start
        i = 1
        while temp is not None:
            output += '{0}{1}{2}'.format(i, temp.getBookID(), temp.gettitle)
            temp = temp.getpointer()
            i += 1
        output += " None"
        return output

    def isempty(self):
        return self.__start is None

    def addnode(self, id, title):
        newwnode = BookRec(ID, title)
        if self.isempty():
            self.__start = None

        else:
            temp = self.start
            self.start = newnode
            newnode.setpointer(temp)

    def delnode(self, id):
        if self.start is not None:
            prev = None
            current = self.start
            while current.getbookid() != id and current.getpointer() is not none:
                prev = current
                current = current.getpointer()
            if prev is None:
                if self.start.getbookid() == id:
                    self.start = current.getpointer()
            elif current.getbookid() == id:
                prev.setpointer(current.getpointer())
