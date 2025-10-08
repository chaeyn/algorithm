n, m = map(int, input().split())
board = [input() for _ in range(n)]

res = 9999

for row in range(n - 7):
    for col in range(m - 7):

        type1 = 0  # W 시작 체스판
        type2 = 0  # B 시작 체스판

        # 각 칸 확인
        for i in range(8):
            for j in range(8):
                now = board[row + i][col + j]

                # 같은 색은 좌표 합이 다 짝수거나 홀수다
                if (i + j) % 2 == 0:
                    if now == "B": type1 += 1  # W여야 하는데 B -> B로 칠하기
                    if now == "W": type2 += 1  # B여야 하는데 W -> W로 칠하기
                else:
                    if now == "W": type1 += 1  # B여야 하는데 W -> W로 칠하기
                    if now == "B": type2 += 1  # W여야 하는데 B -> B로 칠하기

        res = min(res, type1, type2)

print(res)