def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break

    return arr


print(insertion_sort([4, 6, 2, 7, 3, 5, 7, 5]))
