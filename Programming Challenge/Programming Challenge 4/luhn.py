def luhn_verify(id_number):
    """luhn_verify Check if the ID number is luhn valid or not
    
    Arguments:
        id_number {integer} -- Takes in a number for checking
    """

    right_digit = str(id_number)[-1]
    left_digit = str(id_number)[:-1]
    num_arr = []
    counter = 1
    for each in left_digit[::-1]:
        if counter % 2 != 0:
            each = int(each)*2
            each_arr = [int(i) for i in str(each)]
            for num in each_arr:
                num_arr.append(num)

            counter = counter + 1
        else:
            num_arr.append(int(each))
            counter += 1

    total = 0
    for each_number in num_arr:
        total += each_number
    total = total + int(right_digit)
    if total % 10 == 0:
        print("The number is valid")
    else:
        print("The number is not valid")


def gen_valid_id(number):
    if len(number) > 3:
        num_arr = []
        counter = 1
        for each in number[::-1]:
            if counter % 2 != 0:
                each = int(each)*2
                each_arr = [int(i) for i in str(each)]
                for num in each_arr:
                    num_arr.append(num)
                counter += 1
            else:
                num_arr.append(int(each))
                counter += 1
        total = 0
        for each_number in num_arr:
            total += int(each_number)

        check_digit = 10 - (total % 10)
        print("Your check digit is ", check_digit)
        print("Your number is ", str(number)+str(check_digit))

    elif len(number) <= 3:
        print("Please enter a number of minimum 3 digits")


luhn_verify("1762483")
gen_valid_id("176248")
gen_valid_id("23")
gen_valid_id("58136743")
