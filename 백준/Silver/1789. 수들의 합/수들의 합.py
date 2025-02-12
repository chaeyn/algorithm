s = int(input())
i = int(0)
c = int(0)
while True:
    if s > i:
        i += 1
        s -= i
        c += 1
    else:
        print(c)
        break