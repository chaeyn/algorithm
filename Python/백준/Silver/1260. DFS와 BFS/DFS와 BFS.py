n, m, v = map(int, input().split())
dfs_visited = [False]*(n+1)
bfs_visited= dfs_visited.copy()

graph = [[False]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True

def dfs(v):
    dfs_visited[v] = True
    print(v, end=" ")
    for i in range(1, n+1):
        if graph[v][i] is True and dfs_visited[i] is False:
            dfs(i)

def bfs(v):
    queue = [v]
    bfs_visited[v] = True
    while queue:
        v = queue.pop(0) # 방문 노드 제거
        print(v, end=" ")
        for i in range(1, n+1):
            if(bfs_visited[i] is False and graph[v][i] is True):
                queue.append(i)
                bfs_visited[i] = True

dfs(v)
print()
bfs(v)