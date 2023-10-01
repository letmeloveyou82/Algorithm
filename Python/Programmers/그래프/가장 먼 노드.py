from collections import deque
def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        n = q.popleft()
        for i in graph[n]:
            if visited[i[0]] == 0:
                visited[i[0]] = visited[n] + 1
                q.append(i[0])
    return max(visited)

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for a, b in edge:
        graph[a].append([b, 1])
        graph[b].append([a, 1])
    m = bfs(graph, 1, visited)
    return visited.count(m)