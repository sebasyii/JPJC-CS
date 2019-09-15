def binary_search(arr, start, end, element):
    if end >= 1:
        mid = int((start + end) / 2 + 1)

        if arr[mid] == element:
            return mid

        # If element is smaller
        elif arr[mid] > element:
            return binary_search(arr, start, mid - 1, element)

        # element is bigger
        else:
            return binary_search(arr, mid + 1, end, element)

    else:
        return False
