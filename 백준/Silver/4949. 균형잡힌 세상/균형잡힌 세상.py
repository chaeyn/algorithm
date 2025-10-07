import sys
while True:
    stat = sys.stdin.readline().rstrip()
    if stat == ".":
        break
    stack = []
    balanced = True
    for ch in stat:
        if ch in "({[": stack.append(ch)
        elif ch in ")}]":
            if not len(stack): balanced = False
            else:
                left = stack.pop()
                if (left == "(" and ch != ")" or
                    left == "{" and ch != "}" or
                    left == "[" and ch != "]"):
                    balanced =  False
    if balanced and not stack: print("yes") # 괄호검사 통과 && 스택 비어있으면 yes
    else: print("no")