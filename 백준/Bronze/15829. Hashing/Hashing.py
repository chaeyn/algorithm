l = int(input())
alpabet = input()
result = []
res = 0
for i in alpabet:
    result.append(ord(i) - 96)
for i in range(len(result)):
    result[i] = result[i] * 31 ** i
    res += result[i]
print(res%1234567891)