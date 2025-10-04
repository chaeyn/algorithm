import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    co = sys.stdin.readline().split()

    if co[0] == "push":
        stack.append(int(co[1]))
    elif co[0] == "pop":
        if stack: print(stack.pop())
        else: print(-1)
    elif co[0] == "size":
        print(len(stack))
    elif co[0] == "empty":
        if stack: print(0)
        else: print(1)
    elif co[0] == "top":
        if stack: print(stack[-1])
        else: print(-1)
