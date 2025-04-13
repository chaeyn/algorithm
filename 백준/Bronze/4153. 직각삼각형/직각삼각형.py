while True:
    a, b, c = map(int, input().split())
    if a + b + c == 0:
        break
    n = [a, b, c]
    n.sort()
    n[0]*=n[0]; n[1]*=n[1]; n[2]*=n[2]
    if n[0] + n[1] == n[2]:
        print("right")
    else: 
        print("wrong")