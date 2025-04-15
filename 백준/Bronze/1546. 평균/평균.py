n = int(input())
score = list(map(int, input().split()))
max_score = max(score)
new_sum = 0
for i in range(n):
    score[i] = int(score[i]) / max_score * 100
    new_sum += score[i]
print(f"{new_sum / n}")
