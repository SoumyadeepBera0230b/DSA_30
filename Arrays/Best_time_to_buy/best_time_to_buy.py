arr = [2, 9, 1,7, 6, 3]
best_buy = arr[0]
best_sell = arr[0]
profit = 0
count = 0

for i in range(1, len(arr)-1):
    if arr[i] < best_buy:
        best_buy = arr[i]
        best_buy_index = i
        count = 1
    if count == 1 and arr[i] > best_sell and i > best_buy_index:
        best_sell = arr[i]

# for i in range(best_buy_index, len(arr)):
#     if arr[i] > best_sell:
#         best_sell = arr[i]

profit = best_sell - best_buy
print(profit)