t = int(input())
i = int(0)
for i in range(t):
    a = list(map(str, input().split())) 
    n = float(a[0])
    for j in range(len(a)):
        if a[j] == '@':
            n *= 3
        elif a[j] == '%':
            n += 5
        elif a[j] == '#':
            n -= 7
    n = format(n, ".2f")
    print(n)