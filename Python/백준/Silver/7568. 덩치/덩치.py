n = int(input())
people = []
for _ in range(n):
    w, h = map(int, input().split())
    people.append((w, h))
ranks = []
for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)
print(*ranks)