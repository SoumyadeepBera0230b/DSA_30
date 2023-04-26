'''This python file is created to solve the merge_overlapping of the arrays'''

arr = [[1, 3], [2, 5], [4, 9]]
li = [arr[0]]

for i in range(1, len(arr)):
    if li[-1][-1] > arr[i][0]:
        if li[-1][-1] < arr[i][-1]:
            li.append([li[-1][0], arr[i][-1]])
            li.pop(-2)
        else:
            li.append([li[-1][0], li[-1][-1]])
            li.pop(-2)
    else:
        li.append([arr[i][0], arr[i][-1]])
print(li)
print(__doc__)
