def sort(arr):
    for i in range(1, len(arr)-1):
        j = i-1
        ele = arr[i]
        while j >= 0:
            arr[j+1] = arr[j]
            j -= 1
        if j == -1:
            arr[j+1] = ele
    return (arr)
