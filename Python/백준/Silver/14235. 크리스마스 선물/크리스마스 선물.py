import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    x = list(map(int, sys.stdin.readline().split()))
    a = x[0]

    if a == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        for i in range(1, a+1):
            heapq.heappush( heap, -x[i])