t = int(input())
for i in range(t):
  num = list(map(int, input().split()))
  num.remove(max(num))
  num.remove(min(num))
  if max(num) - 4 >= min(num):
    print("KIN")
  else:
    print(sum(num))