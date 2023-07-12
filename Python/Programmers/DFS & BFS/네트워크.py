from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
    return 1

def solution(n, computers):
    result = 0
    visited = [False] * n
    graph = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    for i in range(n):
        if len(graph[i]) == 0:
            result += 1
        elif visited[i] == False:
            result += bfs(graph, i, visited)

    return result