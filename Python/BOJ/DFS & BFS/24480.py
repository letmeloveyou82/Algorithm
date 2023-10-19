import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split()) # 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [0] * (n+1)
cnt = 1

def dfs(r):
    global cnt
    visited[r] = cnt
    graph[r].sort(reverse=True)
    for i in graph[r]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(r)
for i in range(1, n+1):
    print(visited[i])