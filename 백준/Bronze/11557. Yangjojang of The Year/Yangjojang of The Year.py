t = int(input())
for i in range(t):
    n = int(input())
    lst_n = []
    lst_l = []
    for j in range(n):
        n, l = input().split()
        lst_n.append(n)
        lst_l.append(int(l))
    a = lst_l.index(max(lst_l))
    print(lst_n[a])