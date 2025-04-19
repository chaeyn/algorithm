arr = []
for i in range(5):
  ar = list(input())
  arr.append(ar)

for i in range(15):
  for j in range(5):
    if i < len(arr[j]):
      print(arr[j][i], end='')