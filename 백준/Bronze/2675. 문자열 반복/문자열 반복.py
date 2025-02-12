n = int(input())
for i in range(n):
    a, b = input().split()
    for j in range(len(b)):
        a = int(a)
        b = list(b)
        print(a*b[j], end='')
    print()