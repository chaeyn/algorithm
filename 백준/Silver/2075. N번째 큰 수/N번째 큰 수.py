import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    line = (list(map(int, sys.stdin.readline().split())))

    for num in line:
        heapq.heappush(heap, num)
    
        if len(heap) > n: # 가장 큰 n개만 남기면 그 중 최솟값이 n번째 큰 수이다
            heapq.heappop(heap)

print(heap[0])

