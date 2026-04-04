from collections import deque
import sys

queue = deque()

T = int(input())
for i in range(T):
    command = list(sys.stdin.readline().split())
    if command[0] == "push": queue.append(command[1])
    elif command[0] == "pop":
        if not len(queue): print(-1)
        else: print(queue.popleft())
    elif command[0] == "size": print(len(queue))
    elif command[0] == "empty":
        if not len(queue): print(1)
        else: print(0)
    elif command[0] == "front":
        if not len(queue): print(-1)
        else: print(queue[0])
    elif command[0] == "back":
        if not len(queue): print(-1)
        else: print(queue[-1])