k, n, m = map(int, input().split())
k *= n
m -= k
if m>=0 :
    print("0")
else :
    print(-m)