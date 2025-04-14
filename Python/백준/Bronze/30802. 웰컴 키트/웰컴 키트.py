n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
res_t = 0; res_p = n//p; res_p1 = n%p

for i in size:
    if i == 0:
        continue
    elif i <= t:
        res_t += 1
    elif i % t != 0:
        res_t += (i//t)+1
    elif i % t == 0:
        res_t += i//t

print(res_t)
print(res_p, res_p1)