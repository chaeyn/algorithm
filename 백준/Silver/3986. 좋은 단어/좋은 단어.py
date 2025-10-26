def is_good(elem):
    if len(elem) % 2 == 1:
        return False
    s = []
    for i in elem:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
    return len(s) == 0

n = int(input())
cnt = 0
for i in range(n):
    elem = input()
    if is_good(elem):
        cnt += 1
print(cnt)