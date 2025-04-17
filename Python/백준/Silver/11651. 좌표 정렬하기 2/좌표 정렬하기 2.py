n = int(input())
points = []
for i in range(n):
    [x, y] = map(int, input().split())
    points.append([x, y])
points = sorted(points, key= lambda p : (p[1], p[0]))
for p in points:
    print(p[0], p[1])
