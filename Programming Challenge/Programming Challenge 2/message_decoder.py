uppercase_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                      "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercase_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
punctuation_list = ["!", "?", ",", ".", " ", ";", "\"", "'"]

text = open("textstream.txt", "r")
line = text.readline()
text.close()

def decoder():
    decoded_letters = ""
    mode = 0
    text_stream = line.split(",")
    for text in text_stream:
        if mode == 0:
            if (int(text) % 27) != 0:
                decoded_letters = decoded_letters + \
                    uppercase_alphabet[(int(text) % 27) - 1]
            else:
                mode = (mode + 1) % 3

        elif mode == 1:
            if (int(text) % 27) != 0:
                decoded_letters = decoded_letters + \
                    lowercase_alphabet[(int(text) % 27) - 1]
            else:
                mode = (mode + 1) % 3
        elif mode == 2:
            if (int(text) % 9) != 0:
                decoded_letters = decoded_letters + \
                    punctuation_list[(int(text) % 9) - 1]
            else:
                mode = (mode + 1) % 3
    return decoded_letters


def encoder():
    text_list = []
    user_input = input("Enter your sentence(First letter must be uppercase): ")
    text_list = user_input.split()


print(decoder())
