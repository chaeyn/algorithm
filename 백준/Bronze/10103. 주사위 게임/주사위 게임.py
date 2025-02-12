n = int(input())
chang = int(100)
sang = int(100)
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        sang -= a
    elif b > a:
        chang -= b
print(chang)
print(sang)