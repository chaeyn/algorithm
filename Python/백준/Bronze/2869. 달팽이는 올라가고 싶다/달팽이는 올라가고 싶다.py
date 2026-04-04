d, n, m = map(int, input().split())
if d >= m:
    print(1)
else:
    if (m-d) % (d-n) == 0:
        # 목표까지 남은 거리를 (m-d)
        # 하루에 전진하는 거리로 (d-n) 나눴을 때
        # 딱 떨어지지 않으면 하루 더 필요하다는 뜻
        print((m-d)//(d-n)+1)
        # 시작일이 1이므로 1 추가
    else:
        print((m-d)//(d-n)+2)
        # 2인 이유는 마지막 날 추가