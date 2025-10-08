from collections import deque

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    important_degree = list(map(int, input().split()))

    queue = deque()
    for j in range(n):
        queue.append((j, important_degree[j]))

    print_count = 0
    while queue:
        if max(queue, key=lambda x : x[1])[1] != queue[0][1]: # max의 key 매개변수로 우선순위가 높은 것을 찾고 지금 맨 첫번째의 우선순위코다 크면
            queue.append(queue.popleft()) # 맨 첫번째꺼 빼고 맨 뒤로 보내기
        else:
            idx, important = queue.popleft() # 맨 앞에꺼가 우선순위 가장 크다면 빼기
            print_count += 1
            if idx == m: # 출력한게 원래 보기로 했던 번호라면 print count 출력 후 중단
                print(print_count)
                break