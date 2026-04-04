from collections import deque
import sys

t = int(sys.stdin.readline())

q = deque()

for i in range(t):
    co = sys.stdin.readline().split()
    if co[0] == "push_front": q.appendleft(co[1])
    elif co[0] == "push_back": q.append(co[1])
    elif co[0] == "pop_front":
        if len(q) != 0:
            res = q.popleft()
            if res: print(res)
        else: print(-1)
    elif co[0] == "pop_back":
        if len(q) != 0:
            res = q.pop()
            if res: print(res)
        else: print(-1)
    elif co[0] == "size":
        print(len(q))
    elif co[0] == "empty":
        if len(q) == 0: print(1)
        else: print(0)
    elif co[0] == "front":
        if len(q) != 0:
            if q[0]: print(q[0])
        else: print(-1)
    elif co[0] == "back":
        if len(q) != 0:
            if q[-1]: print(q[-1])
        else: print(-1)