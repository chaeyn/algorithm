import sys
input = sys.stdin.readline
n = int(input())
cnt = [0] * n
for i in range(n):
    num = int(input())
    cnt[i] += num
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])