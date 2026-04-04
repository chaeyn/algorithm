dad_body, dad_tail = input().split()
mom_body, mom_tail = input().split()

combi = []

for i in [dad_body, dad_tail, mom_body, mom_tail]:
    for j in [dad_body, dad_tail, mom_body, mom_tail]:
        combi.append((i, j))

combi = set(combi)
res = list(combi)
res.sort()

for body, tail in res:
    print(body, tail)