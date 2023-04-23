arr = [2, 1, 3]
arr = [1, 2, 3]
arr = [1, 3, 2]
arr = [3, 2, 1]

i = len(arr)-2

while i >= 0:
    if arr[i] < arr[i+1]:
        print("Drop found")
        break
    i -= 1

if i == -1:
    # Reversing
    for i in range(len(arr)//2):
        arr[i] = arr[i] + arr[len(arr)-i-1]
        arr[len(arr)-i-1] = arr[i] - arr[len(arr)-i-1]
        arr[i] = arr[i] - arr[len(arr)-i-1]
    print(arr)
else:
    j = len(arr)-1

    while arr[j] < arr[i]:
        j -= 1

    # Swapping
    arr[i] = arr[i] + arr[j]
    arr[j] = arr[i] - arr[j]
    arr[i] = arr[i] - arr[j]
    print(arr, i)
    # arr[i+1::] = arr[-1:i:-1]
    count = 0
    
    for k in range(i+1, len(arr)//2 + 1):
        temp = arr[k]
        arr[k] = arr[len(arr)-1-count]
        arr[len(arr)-1-count] = temp
        print(arr)
        count += 1
        k += 1
    print(arr)
