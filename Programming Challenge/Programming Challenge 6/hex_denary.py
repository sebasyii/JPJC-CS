hexadecimal = str(input("Enter hexadecimal to convert to denary: "))
# change from hexadecimal to binary then to denary
def validation(hexadecimal):
    for each in hexadecimal:
        if each not in "0123456789ABCDEF":
            print("Invalid")
        else:
            continue


# def HToD(hexadecimal):
#     hexadecimalDic = {'0':0, '1':1 , '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
#     total = 0
#     for i in range(len(hexadecimal)-1, -1, -1):
#         total = total + (16**(len(hexadecimal)-1-i))*hexadecimalDic[hexadecimal[i]]
#     return total
# print(HToD('9F'))


def hex_to_denary(hexadecimal):
    hexadecimalDic = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
    power = 0
    total = 0
    for char in hexadecimal[::-1]:
        total += hexadecimalDic[char] * (16 ** power)
        power += 1
    return total


print(hex_to_denary(hexadecimal))

remainderList = []


def denary_to_hex(denary):
    remainder = denary % 16
    remainderList.append(remainder)
    quotient = denary // 16
    if quotient != 0:
        return denary_to_hex(quotient)


denary_to_hex(189)
denary_list = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
]
remainderList = [denary_list[idx] for idx in remainderList[::-1]]
print("".join(remainderList))
