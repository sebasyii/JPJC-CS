def validate_freq(freq):
    if not freq.isdigit():
        print("Error! Enter a number between 0 and 60.")
        return False

    if int(freq) < 0 or int(freq) > 60:
        print("Error! Enter a number between 0 and 60")
        return False
    return True


def task1():
    xlist = list()
    freqlist = list()
    for i in range(6):
        x = input("Next X value ... <ZZZ to END> ")
        if x == "ZZZ":
            break
        else:
            xlist.append(x)
            freq = input("Frequency ... ")
            while not validate_freq(freq):
                freq = input("Frequency ... ")
            freqlist.append(int(freq))
    print()
    print("+" * 40)
    print("Frequency distribution")
    print("+" * 40)
    print()
    for i in range(len(xlist)):
        print("{:2}{:<9}{:<60}".format("", xlist[i], "@" * freqlist[i]))


def task2():
    xlist = list()
    freqlist = list()
    for i in range(6):
        x = input("Next X value ... <ZZZ to END> ")
        if x == "ZZZ":
            break
        else:
            xlist.append(x)
            freq = input("Frequency ... ")
            while not validate_freq(freq):
                freq = input("Frequency ... ")
            freqlist.append(int(freq))
    print()
    print("+" * 40)
    print("Frequency distribution")
    print("+" * 40)
    print()
    num_of_lines = 36 // len(xlist)
    for i in range(len(xlist)):
        print("{:2}{:<9}{:<60}".format("", xlist[i], "+" * freqlist[i]))
        for j in range(num_of_lines - 1):
            print("{:2}{:<9}{:<60}".format("", "", "+" * freqlist[i]))


def task3():
    xlist = list()
    freqlist = list()
    max_freq = 0
    for i in range(6):
        x = input("Next X value ... <ZZZ to END> ")
        if x == "ZZZ":
            break
        else:
            xlist.append(x)
            freq = input("Frequency ... ")
            if int(freq) > max_freq:
                max_freq = int(freq)
            freqlist.append(int(freq))

    scale_freqlist = list()
    if max_freq > 60:
        for freq in freqlist:
            scale_freq = (freq / max_freq) * 60
            scale_freqlist.append(int(scale_freq))
    else:
        scale_freqlist = freqlist
    print(scale_freqlist)
    print()
    print("+" * 40)
    print("Frequency distribution")
    print("+" * 40)
    print()
    num_of_lines = 36 // len(xlist)
    for i in range(len(xlist)):
        print("{:2}{:<9}{:<60}".format("", xlist[i], "\u2588" * scale_freqlist[i]))
        for j in range(num_of_lines - 1):
            print("{:2}{:<9}{:<60}".format("", "", "\u2588" * scale_freqlist[i]))

    print()
    print("{:^11}{:60}".format("X Values", "-" * 60))

    show_value = list()
    if max_freq > 60:
        for i in range(6):
            value = (max_freq / 6) * (i + 1)
            show_value.append(round(value, 1))
    else:
        for i in range(1, 7):
            show_value.append(i * 10)

    print(
        "{:>11}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}".format(
            "0",
            str(show_value[0]),
            str(show_value[1]),
            str(show_value[2]),
            str(show_value[3]),
            str(show_value[4]),
            str(show_value[5]),
        )
    )


task3()
