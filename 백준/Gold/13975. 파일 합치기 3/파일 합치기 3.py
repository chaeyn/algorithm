import heapq
import sys

T = int(input())
for i in range(T):
    k = int(input())
    novels = list(map(int, sys.stdin.readline().split()))
    novels.sort()

    heap = [0]

    heapq.heapify(novels)

    total_cost = 0

    while len(novels) > 1:
        first = heapq.heappop(novels)
        second = heapq.heappop(novels)
        cost = first + second

        total_cost += cost

        heapq.heappush(novels, cost)
    print(total_cost)