A = int(input())
B = int(input())
C = int(input())

res = A * B * C
digits = list(map(int, str(res)))
count = [0]*10

for digit in digits:
    count[digit] += 1

for i in count:
    print(i)
