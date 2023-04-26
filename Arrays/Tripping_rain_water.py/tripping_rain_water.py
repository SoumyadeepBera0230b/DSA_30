arr = [2, 0, 1, 6, 3, 6]
water = 0

for i in range(1, len(arr)-1):
    left_max = arr[0]
    right_max = arr[len(arr)-1]
    for j in range(i+1):
        if arr[j] > left_max:
            left_max = arr[j]
        
    for k in range(i, len(arr)-1):
        if arr[k] > right_max:
            right_max = arr[k]
    print(arr[i], left_max, right_max)
    
    water = water + (min(left_max, right_max) - arr[i])

# left_max = arr[0]
# left_arr = []
# right_max = arr[len(arr)-1]
# right_arr = []

# for i in range(len(arr)):
#     if arr[i] > left_max:
#         left_max = arr[i]
#     left_arr += [left_max]

# for i in range(len(arr)):
#     if arr[i] > right_max:
#         right_max = arr[i]
#     right_arr += [right_max]

# print(right_arr)
# print(left_arr)

# for i in range(len(arr)):
#     water += min(left_arr[i], right_arr[i]) - arr[i]

print(water)
