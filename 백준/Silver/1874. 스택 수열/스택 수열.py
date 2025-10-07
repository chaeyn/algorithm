T = int(input())
stack, res = [], []
current = 1

for i in range(T):
    target = int(input()) # 만들어야 하는 숫자
    while target >= current: # 현재 숫자가 만들어야 하는 숫자가 될 때 까지 반복
        stack.append(current) # 현재 숫자 스택에 push
        current += 1 # 현재 숫자 ++
        res.append("+")
    if stack[-1] == target: # 스택의 마지막 숫자가 만들어야 하는 숫자인 경우 빼내기
        stack.pop()
        res.append("-")
    else:
        print("NO")
        exit()
for i in res:
    print(i)
