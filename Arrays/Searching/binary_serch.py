import sys
sys.path.append('Strings')

from Sorting import bubble_sort as b
arr = [2, 3, 11, 9]
target = 9

b.sort(arr)
left = 0
right = len(arr)-1


while left <= right:
    mid = (right+left)//2

    if arr[mid] > target:
        right = mid-1
    elif arr[mid] < target:
        left = mid+1

    if arr[mid] == target:
        print("found at index:%d"%target)
        break

