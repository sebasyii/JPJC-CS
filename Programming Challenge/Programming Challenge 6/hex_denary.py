hexadecimal_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def main():
    hexa_input = input("Enter your hexadecimal: ")

    for hexa in hexa_input:
        if hexa in hexadecimal_list:
            pass
        else:
            print("This is invalid")
    
    

def calculate_denary(hexa):
    if hexadecimal_list.index(hexa) > 9:
        dec = int(hexa) * 16
    else:
        dec = int(hexa)
    return dec