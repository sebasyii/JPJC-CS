def bubble_sort(arr):
    len_of_arr = len(arr)
    if len_of_arr <= 1:
        return arr
    
    else:
        for i in range(len_of_arr):
            for j in range(len_of_arr-i-1):
                if arr[j] > arr[j+1]:
                    arr[j+1], arr[j] = arr[j], arr[j+1]
                else:
                    continue
        return arr


print(bubble_sort([1,2,4,6,3,7,2]))