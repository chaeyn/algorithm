def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)
n = int(input())
n = str(fac(n))
cnt = 0
while n[-1] == '0':
    cnt += 1
    n = n[:-1]
print(cnt)