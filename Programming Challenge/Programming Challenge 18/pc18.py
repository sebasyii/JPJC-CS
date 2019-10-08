class Record:
    def __init__(self, PersonName="", TelephoneNumber=""):
        self.__PersonName = PersonName
        self.__TelephoneNumber = TelephoneNumber

    def getPersonName(self):
        return self.__PersonName

    def getTelephoneNumber(self):
        return self.__TelephoneNumber

    def setPersonName(self, PersonName):
        self.__PersonName = PersonName

    def setTelephoneNumber(self, TelephoneNumber):
        self.__TelephoneNumber = TelephoneNumber


class Hashtable:
    def __init__(self, size=500):
        self.__size = size
        self.__records = [Record() for i in range(size)]

    def DisplayValues(self):
        print(
            "{0:^10} | {1:^25} | {2:^20}".format(
                "Index", "Person Name", "Telephone Number"
            )
        )
        for element in range(self.__size):

            if (
                self.__records[element].getPersonName() != ""
                and self.__records[element].getTelephoneNumber() != ""
            ):
                print(
                    "{0:^10} | {1:^25} | {2:<20}".format(
                        element,
                        str(self.__records[element].getPersonName()),
                        str(self.__records[element].getTelephoneNumber()),
                    )
                )

    def ReadRecords(self):
        infile = open("HASHEDDATA.txt", "r")

        for line in infile:
            index, person_name, telephone_number = line[:-1].split(",")

            self.__records[int(index)].setPersonName(person_name)
            self.__records[int(index)].setTelephoneNumber(telephone_number)

        infile.close()

    # Convert data to index
    def GenerateHash(self, SearchName):
        HashTotal = int(0)
        index = 1
        for char in SearchName:
            code = ord(char)
            code_weight = code * index
            index += 1
            HashTotal += code_weight

        Hash = HashTotal % 500
        return Hash

    def search(self, data):
        hashcode = self.GenerateHash(data)
        if self.__records[hashcode].getPersonName() == data:
            return f"Index: {hashcode} Person Name: {self.__records[hashcode].getPersonName()} Telephone Number:{self.__records[hashcode].getTelephoneNumber()}"
        else:  # data not found at hashcode location
            nextslot = self.rehash(hashcode)
            while self.__records[nextslot].getPersonName() != data:
                nextslot = self.rehash(nextslot)
                if self.__records[nextslot].getPersonName() == data:
                    return f"Index: {hashcode} Person Name: {self.__records[hashcode].getPersonName()} Telephone Number:{self.__records[hashcode].getTelephoneNumber()}"
                else:
                    return "Not FOUND"

    def rehash(self, oldhash):
        return (oldhash + 1) % 500


def main():
    records = Hashtable()
    records.ReadRecords()
    records.DisplayValues()
    print(records.GenerateHash("Tait Davinder"))
    print(records.GenerateHash("Anandan Yeo"))
    print(records.search("Charlie Love"))
    print(records.search("Chin Tan"))
    print(records.search("John Barrowman"))


main()
