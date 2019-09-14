def LicenceKey():
    import random
    key = ''
    total = int(0)
    for i in range(1,10):
        asciiCode = random.randint(65,65+25)
        letter = chr(asciiCode)
        key = key + letter
        total = total + asciiCode*(i)
    remainder = total % 11
    if remainder == 10:
        remainder = 'X'
    key = str(key) + str(remainder)
    return key

##for i in range(3):
##    print(LicenceKey())

def menu():
    while True:
        print("1. Purchase of a new licence for either a single-user or 3-user licence")
        print("2. Register an additional user to an active 3-user licence")
        print("3. End")
        choice = input("Enter your option: ")

        if choice == '1':
            licenceType = input("Enter type of licence (S)ingle/(3)-user: ")
            if licenceType == 'S':
                key = LicenceKey() + ' 1'
            elif licenceType == '3':
                key = LicenceKey() + ' 3 1'
            else:
                print("Invalid licence type selected.")
                continue
            print(key, "licence key issued.")
            outfile = open("LICENCE-KEYS.txt", "a")
            outfile.write(str(key))
            outfile.write('\n')
            outfile.close()
            infile = open("LICENCE-KEYS.txt", "r")
            for line in infile:
                print(line[:-1])
            infile.close()
        elif choice == '2':
            userKey = input("To register new user. Enter licence key: ")
            licenceList = list()
            infile = open("LICENCE-KEYS.txt", "r")
            for line in infile:
                licenceList.append(line[:-1])
            infile.close()

            for eachKey in licenceList:
                if userKey == eachKey[0:10]:
                    keyIndex = licenceList.index(eachKey)
                    if int(licenceList[keyIndex][-3:-1]) == 3:
                        if int(licenceList[keyIndex][-1:]) == 1:
                            licenceList[keyIndex] = licenceList[keyIndex][:-2] + ' 2'
                        elif int(licenceList[keyIndex][-1:]) == 2:
                            licenceList[keyIndex] = licenceList[keyIndex][:-2] + ' 3'
                        else:
                            print(f"{licenceList[keyIndex][:-3]} is full")

            outfile = open("LICENCE-KEYS.txt", "w")
            for licence in licenceList:
                outfile.write(licence)
                outfile.write('\n')
            outfile.close()

        elif choice == '3':
            print("Exit Program")
            break

        else:
            print("Invalid option selected. Try again")
            continue
    
menu()

class Licence:
    def __init__(self, key='', licenceType='', date='', name=''):
        self.__LicenceKey = key
        self.__LicenceType = licenceType
        self.__DateOfPurchase = date
        self.__name = name

    def setLicenceKey(self, key):
        self.__LicenceKey = key

    def getLicenceKey(self):
        return self.__LicenceKey

    def setLicenceType(self, licenceType):
        self.__LicenceType = licenceType

    def getLicenceType(self):
        return self.__LicenceType

    def setDateOfPurchase(self, date):
        self.__DateOfPurhcase = date

    def getDateOfPurchase(self):
        return self.__DateOfPurchase

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class SingleUser(Licence):
    def __init__(self, mac='', dateRegister=''):
        self.__MACaddress = mac
        self.__dateReg = dateRegister
        Licence.__init__(self, key='', licenceType='', date='', name='')
        #super().init()

    def setMACaddress(self, mac):
        self.__MACaddress = mac

    def getMACaddress(self):
        return self.__MACaddress

    def setDateReg(self, dateReg):
        self.__dateReg = dateReg

    def getDateReg(self):
        return self.__dateReg

    def display(self):
        pass

class ThreeUser(Licence):
    def __init__(self, mac='', dateRegister='', number=1):
        self.__MACaddress = mac
        self.__dateReg = dateRegister
        self.__numberOfUser = number
        Licence.__init__(self, key='', licenceType='', date='', name='')

    def setMacAddress(self, mac):
        self.__MACaddress = mac

    def getMacAddress(self):
        return self.__MACaddress

    def setDateReg(self, dateReg):
        self.__dateReg = dateReg

    def getDateReg(self):
        return self.__dateReg

    def setNumberOfUser(self, number):
        self.__numberOfUser = number

    def getNumberOfUser(self):
        return self.__numberOfUser

    def display(self): #to show polymorphism
        pass
    
            
