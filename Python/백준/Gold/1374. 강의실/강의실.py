import heapq
import sys

T = int(input())
lectures = []

for _ in range(T):
    num, start, end = list(map(int, sys.stdin.readline().split()))
    lectures.append((start, end))

lectures.sort() # 시작 시간 기준 정렬

heap = []

for start, end in lectures:
    # heap[0] -> 가장 빨리 끝나는 강의의 종료 시간, heap[0] <= start이면 그 강의실은 이미 사용이 끝났다
    if heap and heap[0] <= start:
        heapq.heappop(heap) # 사용 끝난 강의실 비우기

    heapq.heappush(heap, end) # 새 강의 강의실에 넣기

print(len(heap))