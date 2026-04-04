from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()

    if n == 0:
        deq = deque()
    else:
        deq = deque(map(int, arr[1:-1].split(',')))

    is_reversed = False
    error = False

    for co in p:
        if co == 'R':
            is_reversed = not is_reversed

        elif co == 'D':
            if not deq:
                error = True
                break

            if is_reversed:
                deq.pop()
            else:
                deq.popleft()

    if error:
        print("error")
    else:
        if is_reversed:
            deq.reverse()

        print('[' + ','.join(map(str, deq)) + ']')