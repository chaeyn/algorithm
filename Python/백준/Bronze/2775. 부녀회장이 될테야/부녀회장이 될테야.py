t = int(input())
for i in range(t):
    h = int(input()) # 층 수
    w = int(input()) # 호실 수
    if h == 0: # 0층이면 (호실 숫자 = 인원 수) 출력
        print(w)
        continue
    lst = [i for i in range(1, w+1)] # 0층 1호부터 w호까지 값 지정
    for i in range(1, h+1): # 1층에서 h층까지
        for j in range(1, w): # 1호에서 w-1호까지 
            lst[j] += lst[j-1]
            # (k-1)층 1호부터 w호까지 몇 명이 사는지를 알아야 한다
            # f(k, n) = f(k, n-1) + f(k-1, n)
            # f(k, n-1)은  k-1층의 n-1호까지의 총 인원수
            # f(k-1, n)은 바로 밑층 호수의 사람 수
            # 그러므로 f(k, n-1) + f(k-1, n) = f(k, n)
            # lst[j]는 바로 밑 층 호수의 사람 수, lst[j-1]은 바로 전 호수
            # 그러므로 이 점화식 성립
    print(lst[-1]) # 마지막 호 사람 수출력