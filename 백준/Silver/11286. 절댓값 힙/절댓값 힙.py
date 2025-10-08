import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if heap:
            abs_value, original_value = heapq.heappop(heap)
            print(original_value)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x)) # abs는 절댓값, 절댓값 같으면 음수 먼저