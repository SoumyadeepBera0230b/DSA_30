def sort(arr):
    for i in range(len(arr)-1):
        minima = i+1
        for j in range(i+1, len(arr)):
            if arr[minima] > arr[j]:
                minima = j
        if arr[minima] < arr[i]:
            arr[i], arr[minima] = arr[minima], arr[i]
    return (arr)
