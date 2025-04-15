while True:
    c = ''
    check = False
    n = int(input())
    if n == 0:
        break
    n = str(n)
    for i in range(len(n)-1, -1, -1):
        c += n[i]
        if n == c:
            c = ""
            check = True
            print("yes")
    if check == False:
        print("no")