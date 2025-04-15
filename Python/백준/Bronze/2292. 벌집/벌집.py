n = int(input())
num = 1
for i in range(n):
    num += i*6
    if n <= num:
        print(i+1)
        break