arr = [2, 1, 2, 2, 1, 0, 0]
# [0]

left = 0
mid = 0
right = len(arr) - 1

while mid < right:
    if arr[mid] == 0:
        arr[mid] = arr[left] + arr[mid]
        arr[left] = arr[mid] - arr[left]
        arr[mid] = arr[mid] - arr[left]
        left += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid] = arr[right] + arr[mid]
        arr[right] = arr[mid] - arr[right]
        arr[mid] = arr[mid] - arr[right]
        right -= 1
print(arr)