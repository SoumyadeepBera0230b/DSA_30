def sort(arr):
    if len(arr) == 1:
        return 1
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    sort(left)
    sort(right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if right[j] > left[i]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr
