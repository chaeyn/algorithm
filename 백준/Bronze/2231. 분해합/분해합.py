n = int(input())
r = 0
for i in range(n):
    lst = list(map(int, str(i)))
    if sum(lst) + i == n:
        r = i
        break
print(r)