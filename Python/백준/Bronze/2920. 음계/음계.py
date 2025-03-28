scl = list(map(int, input().split()))

acn = []
mix = []
for i in range(1, 9):
    acn.append(i)
for i in range(8, 0, -1):
    mix.append(i)

if scl == acn:
    print('ascending')
elif scl == mix:
    print('descending')
else:
    print('mixed')