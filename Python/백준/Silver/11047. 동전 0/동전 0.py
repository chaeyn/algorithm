n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

ans = 0
for coin in coins:
    # coins 안에 있는 수 중 k를 나눌 수 있는 가장 큰 수
    if k >= coin:
        ans += k // coin
        k %= coin # 나누고 남은 값 다시 k에 저장 후 반복
        if k <= 0:
            break

print(ans)