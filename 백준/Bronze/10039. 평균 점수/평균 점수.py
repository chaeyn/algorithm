rst = 0
a = [int(input()) for _ in range(5)]
for i in range(5):
    if (a[i] < 40):
        a[i] = 40
    rst += a[i]
print(int(rst/5))