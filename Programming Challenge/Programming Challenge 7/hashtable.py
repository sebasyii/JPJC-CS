class Hashtable:
    def __init__(self, Max = 20):
        self.__size = Max
        self.__data = [None] * self.__size

    def display(self):
        print("{0:^20} | {1:<20}".format("Address","ID"))
        for element in range(self.__size):
            print("{0:^20} | {1:<20}".format(element, str(self.__data[element])))

    # Convert data to index
    def hashfunction(self, keydata):
        total = int(0)
        for char in keydata:
            print("keydata: {0} , char: {1}".format(keydata,char))
            total += ord(char)
            print("Total: {0}".format(total))
        return total % self.__size

    # Convert old hash to new hash
    def rehash(self, oldhash):
        return (oldhash+1)%self.__size

    # Insert data
    def insert(self, data):
        # Convert to index
        hashcode = self.hashfunction(data)
        print(hashcode)
        # if the hash location is not taken, insert the data
        if self.__data[hashcode] is None:
            self.__data[hashcode] = data
        else:
            # Linear probing - next location linearly
            nextslot = self.rehash(hashcode)

            # Check if its taken
            while self.__data[nextslot] is not None:
                # if not rehash again
                nextslot = self.rehash(nextslot)

            # change data
            self.__data[nextslot] = data

    def search(self, data):
        hashcode = self.hashfunction(data) #get the hashcode from the hashfunction
        if self.__data[hashcode] == data: #data is found, return index
            return self.hashfunction(data)
        else: # data not found at hashcode location
            nextslot = self.rehash(hashcode)
            while self.__data[nextslot] != data:
                nextslot = self.rehash(nextslot)
                if nextslot == hashcode:
                    print(data, "not found in hash table")
                    return
            return self.hashfunction(data)

id_file = open("KEYS2.txt", "r")

h1 = Hashtable()
for id in id_file:
    id = id[:-1]
    h1.insert(id)
h1.display()


id_file.close()

id_number = input("Enter an ID Number: ")
print(h1.search(id_number))



