import random


def quick_sort(arr):

    len_of_arr = len(arr)

    if len_of_arr <= 1:
        return arr

    smaller, equal, larger = [], [], []
    pivot = arr[random.randint(0, len_of_arr - 1)]

    for element in arr:
        if element < pivot:
            smaller.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            larger.append(element)

    return quick_sort(smaller) + equal + quick_sort(larger)
