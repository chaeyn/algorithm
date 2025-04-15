n, m = map(int, input().split())
def gcd (n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)
def lcm (n, m):
    return n * m // gcd(n, m)
print(gcd(n, m))
print(lcm(n, m))