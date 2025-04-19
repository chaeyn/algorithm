arr = []
for i in range(9):
    ar = list(map(int, input().split()))
    arr.append(ar)
max_arr = arr[0][0]
max_row = 0
max_col = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_arr:
            max_arr = arr[i][j]
            max_row = i
            max_col = j
print(max_arr)
print(max_row+1, max_col+1)