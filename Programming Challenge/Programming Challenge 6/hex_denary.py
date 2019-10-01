hexadecimal = str(input("Enter hexadecimal to convert to denary: "))
# change from hexadecimal to binary then to denary


def validation(hexadecimal):
    for each in hexadecimal:
        if each not in "0123456789ABCDEF":
            print("Invalid")
        else:
            continue


def hex_to_denary(hexa):
    hexaDec = [
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
    power = 0
    total = 0
    for char in hexa[::-1]:
        if char in hexaDec:
            total += hexaDec.index(char) * (16 ** power)
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
