import heapq
import sys

n = int(input())
tasks = []

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split())
    tasks.append((d, w))

tasks.sort() # 마감일 오름차순 정렬 ex) (1, 20), (2, 50), (3, 30), (4, 10), (4, 40) ...

heap = []

for d, w in tasks:
    heapq.heappush(heap, w) # 과제 점수를 힙에 추가

    if len(heap) > d: # 마감일 d까지 d개의 과제만 가능한데 d개를 초과하면 최솟값을 제거
        heapq.heappop(heap)

print(sum(heap))

