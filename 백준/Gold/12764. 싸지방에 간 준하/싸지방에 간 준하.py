import sys
import heapq

n = int(input())
people = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    people.append((start, end))

people.sort() # 사용 시작 시간 기준 정렬

busy = [] # 사용 중
available = [] # 사용 가능한 자리
usage = {} # 자리 사용 횟수 딕셔너리
next_seat = 1

for start, end in people:
    # 사용 끝난 자리 available로 이동
    while busy and busy[0][0] <= start: # 사용 중인 자리 중 끝나는 시간이 다른 사용자가 시작하는 시간 전에 끝나면
        _, seat_num = heapq.heappop(busy)
        heapq.heappush(available, seat_num)
    # 같은 자리 재사용
    if available:
        seat_num = heapq.heappop(available) # 작은 번호 자리 사용 (문제 조건)
        heapq.heappush(busy, (end, seat_num))
        usage[seat_num] += 1
    # 자리 아예 없거나 처음 손님이면 새로 만들기
    else:
        seat_num = next_seat
        usage[next_seat] = 1
        heapq.heappush(busy, (end, next_seat))
        next_seat += 1

print(next_seat - 1)
print(*[usage[i] for i in range(1, next_seat)])