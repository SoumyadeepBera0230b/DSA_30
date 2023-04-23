arr = [3, 4, 1, -5, -8, 2]

current_sum = 0
overall_sum = arr[0]

for i in range(len(arr)):
    if current_sum < 0:
        current_sum = 0
    current_sum += arr[i]
    
    overall_sum = max(current_sum, overall_sum)

print(overall_sum)