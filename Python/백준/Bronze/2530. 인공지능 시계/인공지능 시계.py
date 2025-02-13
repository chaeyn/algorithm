h, m, s = map(int, input().split())
t = int(input())
s += t
if s > 59:
    m += (s // 60)
    s = (s % 60)
if m > 59:
    h += (m // 60)
    m = (m % 60)
if h > 23:
    h = h % 24

print(h, m, s)

