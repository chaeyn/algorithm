w = input().upper()
apbet_cnt = [0]*26
for i in w:
    apbet_cnt[ord(i) - 65] += 1

max_cnt = max(apbet_cnt)
max_data = []
for i in range(len(apbet_cnt)):
    if apbet_cnt[i] == max_cnt:
        max_data.append(i)

if len(max_data) > 1:
    print("?")
else:
    print(chr(max_data[0] + 65))