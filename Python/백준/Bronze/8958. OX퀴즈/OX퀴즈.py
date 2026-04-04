t = int(input())
for _ in range(t):
    quiz = input()
    point = 0
    streak = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            streak += 1
            point += streak
        else:
            streak = 0
    print(point)