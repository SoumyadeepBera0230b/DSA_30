arr = [2, 4, 1, 66]
target = 4
found = -1
for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index: %s" %i)
        found = 0
        break
if found:
    print("Not found")