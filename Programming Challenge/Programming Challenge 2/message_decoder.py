from random import randint
uppercase_alphabet = [chr(char) for char in range(65,65+26)]
lowercase_alphabet = [chr(char) for char in range(97,97+26)]
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
    encoded_numbers = ""
    mode = 0
    user_input = input("Enter your sentence(First letter must be uppercase): ")
    text_list = [letters for letters in user_input]
    for text in text_list:
        if text in uppercase_alphabet:
            if mode == 1:
                encoded_numbers = encoded_numbers + str(0) + ","
                encoded_numbers = encoded_numbers + str(0) + ","
            elif mode == 2:
                encoded_numbers = encoded_numbers + str(0) + ","

            mode = 0
            index_element = uppercase_alphabet.index(text)
            encoded_number = (index_element+1) + 27 * 1
            encoded_numbers = encoded_numbers + str(encoded_number) + ","
        elif text in lowercase_alphabet:
            if mode == 0:
                encoded_numbers = encoded_numbers + str(0) + ","

            elif mode == 2:
                encoded_numbers = encoded_numbers + str(0) + ","
                encoded_numbers = encoded_numbers + str(0) + ","
            mode = 1
            index_element = lowercase_alphabet.index(text)
            encoded_number = (index_element+1) + 27 * 1
            encoded_numbers = encoded_numbers + str(encoded_number) + ","
        elif text in punctuation_list:
            if mode == 0:
                encoded_numbers = encoded_numbers + str(0) + ","
                encoded_numbers = encoded_numbers + str(0) + ","
            elif mode == 1:
                encoded_numbers = encoded_numbers + str(0) + ","
            mode = 2
            index_element = punctuation_list.index(text)
            encoded_number = (index_element+1) + 9 * 1
            encoded_numbers = encoded_numbers + str(encoded_number) + ","
    return encoded_numbers[:-1]


def encoder_random():
    encoded_numbers = ""
    mode = 0
    user_input = input("Enter your sentence(First letter must be uppercase): ")
    text_list = [letters for letters in user_input]
    for text in text_list:
        if text in uppercase_alphabet:
            if mode == 1:
                encoded_numbers = encoded_numbers + str(0) + ","
                encoded_numbers = encoded_numbers + str(0) + ","
            elif mode == 2:
                encoded_numbers = encoded_numbers + str(0) + ","

            mode = 0
            index_element = uppercase_alphabet.index(text)
            encoded_number = (index_element+1) + 27 * randint(1, 10)
            encoded_numbers = encoded_numbers + str(encoded_number) + ","
        elif text in lowercase_alphabet:
            if mode == 0:
                encoded_numbers = encoded_numbers + str(0) + ","

            elif mode == 2:
                encoded_numbers = encoded_numbers + str(0) + ","
                encoded_numbers = encoded_numbers + str(0) + ","
            mode = 1
            index_element = lowercase_alphabet.index(text)
            encoded_number = (index_element+1) + 27 * randint(1, 10)
            encoded_numbers = encoded_numbers + str(encoded_number) + ","
        elif text in punctuation_list:
            if mode == 0:
                encoded_numbers = encoded_numbers + str(0) + ","
                encoded_numbers = encoded_numbers + str(0) + ","
            elif mode == 1:
                encoded_numbers = encoded_numbers + str(0) + ","
            mode = 2
            index_element = punctuation_list.index(text)
            encoded_number = (index_element+1) + 9 * randint(1, 10)
            encoded_numbers = encoded_numbers + str(encoded_number) + ","
    return encoded_numbers[:-1]


print(encoder_random())
print(decoder())
