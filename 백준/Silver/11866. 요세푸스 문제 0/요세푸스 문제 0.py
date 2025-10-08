from collections import deque

n, k = map(int, input().split())

queue = deque(range(1, n+1))

arr = []
while queue:
    queue.rotate(-(k-1)) # k-1번 회전해서 k번째를 맨 앞으로 만들기
    arr.append(queue.popleft())

print("<"+", ".join(map(str, arr))+">")