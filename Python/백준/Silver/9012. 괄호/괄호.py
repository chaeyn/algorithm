class Stack:
    def __init__(self):
        self.capacity = 50
        self.array = [None] * self.capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        self.top += 1
        self.array[self.top] = item

    def pop(self):
        item = self.array[self.top]
        self.top -= 1
        return item

def check_brackets(stat):
    stack = Stack()
    for ch in stat:
        # 왼쪽 괄호가 오른쪽 괄호보다 먼저 표기 조건
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.is_empty(): return False
            # 서로 다른 타입의 괄호 쌍이 서로를 교차하면 안되는 조건
            else:
                left = stack.pop()
                if ((ch == "}" and left != "{") or
                    ch == "]" and left != "[" or
                    ch == ")" and left != "("):
                    return False
    # 왼쪽 괄호 개수 == 오른쪽 괄호 개수
    return stack.is_empty()

n = int(input())
for i in range(n):
    bracket = input()
    res = check_brackets(bracket)
    if res: print("YES")
    else: print("NO")