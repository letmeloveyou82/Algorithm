import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 노드 수
p1, p2 = map(int, input().split()) # 촌수 계산해야 하는 노드 번호
m = int(input()) # 간선 수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
visited = [-1] * (n+1)

def dfs(r, cnt):
    visited[r] = cnt
    for i in graph[r]:
        if visited[i] == -1:
            dfs(i, cnt+1)

dfs(p1, 0)
print(visited[p2])