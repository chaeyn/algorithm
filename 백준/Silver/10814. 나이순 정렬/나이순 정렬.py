n = int(input())
user = []
for i in range(n):
    a, b = input().split()
    user.append((int(a), b))
user.sort(key=lambda x: x[0])
for a, b in user:
    print(a, b)