hexadecimal = str(input("Enter hexadecimal to convert to denary: "))
#change from hexadecimal to binary then to denary
def validation(hexadecimal):
    for each in hexadecimal:
        if each not in "0123456789ABCDEF":
            print ("Invalid")
        else:
            continue

def HToD(hexadecimal):
    hexadecimalDic = {'0':0, '1':1 , '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    total = 0
    for i in range(len(hexadecimal)-1, -1, -1):
        total = total + (16**(len(hexadecimal)-1-i))*hexadecimalDic[hexadecimal[i]]
    return total

print(HToD('9F'))