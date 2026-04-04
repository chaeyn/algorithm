max, mp = 0, 0
for i in range(1, 6):
    sum = 0
    score = input().split()
    for s in score:
        sum += int(s)
    if sum >= max:
        max, mp = sum, i
print(mp, max)
