n = int(input())

lst = []
rst = 0

for i in range(n):
  lst.append(input())

recycle = list(map(int, input().split()))
normal = int(input())

recycle_map = {'P': 0, 'C': 1, 'V': 2, 'S': 3, 'G': 4, 'F': 5}

for l in lst:
  if len(set(l)) == 1 and l[0] in recycle_map:
    recylce_cost = len(l) * recycle[recycle_map[l[0]]]
    nomal_cost = len(l) * normal
    rst += min(recylce_cost, nomal_cost)
  else:
      rst += len(l) * normal

print(rst)