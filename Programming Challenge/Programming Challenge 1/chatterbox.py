# Programming Challenge 1: Chatterbox


def main():
    originalWords = getInput()
    chatterbot(originalWords)


def chatterbot(wordList):
    firstHello = False  # keep track of first occurence of "hello"
    for i in range(len(wordList)):
        print("Chatterbot: ", wordList[i])
        if ("hello" in wordList[i].lower()) and (firstHello == (False)):
            print("Chatterbot: Hi, how are you?")
            firstHello = True

        elif ("hello" in wordList[i].lower()) and (firstHello == (True)):
            print("Chatterbot: Hello again, welcome back!")

        elif ("thank you" in wordList[i].lower()) or ("thanks" in wordList[i].lower()):
            print("Chatterbot: You are most welcome.")

        elif ("missed" in wordList[i].lower()):
            print("Chatterbot: You missed me? I really missed you too.")

        elif ("I" in wordList[i] and "you" in wordList[i].lower()):
            sentence = wordList[i].split()
            if sentence[0] == "I" and ("you" in sentence[2].lower()):
                print("Chatterbot: You",
                      sentence[1], "me? I really", sentence[1], "you too.")

        else:
            print("Chatterbot: Sorry, I do not understand...")

        print()


def getInput():  # read data in file
    infile = open("chatterbot.txt", "r")  # open file
    originalWords = []
    for line in infile:  # for each line in file, read data line by line
        originalWords.append(line[:-1])
    infile.close()  # close file
    return originalWords


main()
