t = int(input())
points = []
for i in range(t):
    [x, y] = map(int, input().split())
    points.append([x, y])
points = sorted(points, key = lambda p : (p[0], p[1]))
for p in points:
    print(p[0], p[1])