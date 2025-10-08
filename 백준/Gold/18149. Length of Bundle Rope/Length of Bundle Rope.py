import heapq
import sys

T = int(input())

for _ in range(T):
    n = int(input())
    packages = list(map(int, sys.stdin.readline().split()))

    # package가 한개면 묶을 필요 X -> 비용 0
    if n == "1":
        print(0)
        continue

    heapq.heapify(packages)

    total_cost = 0

    # 하나로 묶이기 전까지
    while len(packages) > 1:
        # 가장 작은 거 두개 묶기
        first = heapq.heappop(packages)
        second = heapq.heappop(packages)
        cost = first + second

        total_cost += cost

        # 가장 작은 거 두개 묶은거 다시 넣어서 또 작으면 새로운거랑 묶어서 반복
        heapq.heappush(packages, cost)
    print(total_cost)