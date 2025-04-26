n = int(input())
p = list(map(int, input().split()))

xor_sum = 0
for stones in p:
    xor_sum ^= stones

if xor_sum == 0:
    print("cubelover")
else:
    print("koosaga")
