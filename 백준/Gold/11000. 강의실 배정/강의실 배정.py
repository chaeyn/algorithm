import sys
import heapq

T = int(input())
meetings = []

for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

meetings.sort()

heap = []

for start, end in meetings:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))