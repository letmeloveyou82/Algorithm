def dfs(start_node, depth):
    global result
    if result < depth:
        result = depth
    for x in graph[start_node]:
        if not visited[x]:
            visited[x] = True
            dfs(x, depth+1)
            visited[x] = False

T = int(input())
for test_case in range(1, T+1):
    result = 1
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    if M != 0:
        for _ in range(M):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)
    for i in range(1, N+1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False
    print(f"#{test_case} {result}")