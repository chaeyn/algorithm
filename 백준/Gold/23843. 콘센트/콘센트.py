import heapq
import sys

n, m = map(int, sys.stdin.readline().split()) # 전자기기수, 콘센트수
times = list(map(int, sys.stdin.readline().split())) # 각 전자기기 충전 필요한 시간
times.sort(reverse=True) # 내림차순, 긴 작업부터 시

# 콘센트 초기화
heap = [0] * m
heapq.heapify(heap)

for time in times:
    fast = heapq.heappop(heap) # 가장 빨리 끝나는 콘센트 종료 시간
    heapq.heappush(heap, fast + time) # 끝난 콘센트에 새로운 기기 추가

print(max(heap))