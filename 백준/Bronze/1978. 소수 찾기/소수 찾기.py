n = int(input())
lst = list(map(int, input().split()))
check = 0
prime_num = 0

for i in range(n):
    check = 0
    for j in range(1, lst[i]+1):
        if lst[i] % j == 0:
            check += 1
    if check == 2:
        prime_num += 1
print(prime_num)