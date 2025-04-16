import sys
input = sys.stdin.readline
cnt = [0] * 10001
n = int(input())
for _ in range(n):
    num = int(input())
    cnt[num] += 1
for i in range(1, 10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)